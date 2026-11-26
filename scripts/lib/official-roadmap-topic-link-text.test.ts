import assert from 'node:assert/strict';
import { test } from 'node:test';
import { parse } from 'node-html-parser';
import { markdownToHtml } from './markdown';
import { formatOfficialRoadmapTopicResourceLink } from './official-roadmap-topic';

const titles = [
  'JavaScript reference',
  'Array [index] and <element>',
  'Understanding *args and **kwargs**',
  'The _private_ field',
  'Using `useEffect` correctly',
  'Deprecated ~~methods~~',
  'Literal \\*stars\\* and [brackets]',
];

for (const title of titles) {
  test(`preserves literal resource title: ${title}`, () => {
    const resource = {
      type: 'article' as const,
      title,
      url: 'https://example.com/guide',
    };
    const markdown = formatOfficialRoadmapTopicResourceLink(resource);
    const root = parse(markdownToHtml(markdown, false));
    const link = root.querySelector('li > a');

    assert.ok(link);
    assert.equal(link.textContent, `@article@${title}`);
    assert.equal(link.getAttribute('href'), resource.url);
    assert.equal(root.querySelector('li')?.textContent, link.textContent);
  });
}
