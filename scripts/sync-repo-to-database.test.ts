import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { test } from 'node:test';

const repoDir = fileURLToPath(new URL('..', import.meta.url));

function syncResources(types: string[]) {
  const content = [
    '# Example',
    '',
    'Topic description.',
    '',
    'Visit the following resources to learn more:',
    '',
    ...types.map(
      (type, index) =>
        `- [@${type}@Resource ${index}](https://example.com/${index})`,
    ),
  ].join('\n');

  // Exercise the CLI through its POST payload without reading a real topic or
  // contacting roadmap.sh. Unexpected network requests fail the test.
  const result = spawnSync(
    process.execPath,
    [
      '--import',
      'tsx',
      '--input-type=module',
      '--eval',
      `
        import assert from 'node:assert/strict';
        import fs from 'node:fs/promises';
        import path from 'node:path';
        const file = 'roadmaps/example/content/example@node-id.md';
        const filePath = path.resolve(file);
        const originalReadFile = fs.readFile;
        const originalStat = fs.stat;
        fs.stat = async (target, ...args) =>
          target === filePath ? {} : originalStat(target, ...args);
        fs.readFile = async (target, ...args) =>
          target === filePath ? ${JSON.stringify(content)} : originalReadFile(target, ...args);
        globalThis.fetch = async (url, options) => {
          if (url === 'https://roadmap.sh/api/v1-official-roadmap/example') {
            return Response.json({ nodes: [{ id: 'node-id', data: { label: 'Example' } }] });
          }
          assert.equal(url, 'https://roadmap.sh/api/v1-sync-official-roadmap-topics');
          assert.equal(options.method, 'POST');
          console.log('PAYLOAD:' + options.body);
          return Response.json({});
        };
        process.argv = [process.execPath, 'sync', '--files=' + file, '--secret=test-only'];
        await import('./scripts/sync-repo-to-database.ts');
      `,
    ],
    { cwd: repoDir, encoding: 'utf8' },
  );

  assert.equal(result.status, 0, result.stdout + result.stderr);
  const payloadLine = result.stdout
    .split('\n')
    .find((line) => line.startsWith('PAYLOAD:'));
  assert.ok(payloadLine, result.stdout);
  const payload = JSON.parse(payloadLine.slice('PAYLOAD:'.length));
  assert.equal(payload.topics.length, 1);
  assert.equal(
    payload.topics[0].description,
    '# Example\n\nTopic description.',
  );
  return payload.topics[0].resources as {
    type: string;
    title: string;
    url: string;
  }[];
}

test('sync orders courses, podcasts and books after official documentation', () => {
  const resources = syncResources([
    'book',
    'video',
    'podcast',
    'course',
    'article',
    'opensource',
    'official',
  ]);
  assert.deepEqual(
    resources.map((resource) => resource.type),
    ['official', 'opensource', 'article', 'course', 'podcast', 'video', 'book'],
  );
});

test('sync includes roadmap and feed resources in the supported type order', () => {
  const resources = syncResources(['feed', 'book', 'official', 'roadmap']);
  assert.deepEqual(
    resources.map((resource) => resource.type),
    ['roadmap', 'official', 'book', 'feed'],
  );
});

test('sync preserves links and relative order within a resource type', () => {
  const resources = syncResources([
    'article',
    'official',
    'unknown',
    'article',
  ]);
  assert.deepEqual(resources, [
    { type: 'official', title: 'Resource 1', url: 'https://example.com/1' },
    { type: 'article', title: 'Resource 0', url: 'https://example.com/0' },
    { type: 'article', title: 'Resource 2', url: 'https://example.com/2' },
    { type: 'article', title: 'Resource 3', url: 'https://example.com/3' },
  ]);
});
