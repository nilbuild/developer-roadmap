import assert from 'node:assert/strict';
import { test } from 'node:test';
import { parse } from 'node-html-parser';
import { markdownToHtml } from './markdown';
import {
  allowedOfficialRoadmapTopicResourceType,
  formatOfficialRoadmapTopicResourceLink,
  prepareOfficialRoadmapTopicContent,
  type OfficialRoadmapTopicContentDocument,
} from './official-roadmap-topic';

const urls = [
  'https://example.com/guide',
  'https://example.com/wiki/Function_(mathematics)',
  'https://example.com/search?q=call(',
  'https://example.com/search?q=call)',
  'https://example.com/search?q=(one))&lang=en#section',
  'https://example.com/search?q=%28call%29',
];

for (const url of urls) {
  test(`preserves resource destination: ${url}`, () => {
    const resource = { type: 'official' as const, title: 'Reference', url };
    const markdown = formatOfficialRoadmapTopicResourceLink(resource);
    const root = parse(markdownToHtml(markdown, false));
    const link = root.querySelector('li > a');

    assert.ok(link);
    assert.equal(link.getAttribute('href'), url);
    assert.equal(link.textContent, '@official@Reference');
    assert.equal(root.querySelector('li')?.textContent, link.textContent);
  });
}

function createTopic(): OfficialRoadmapTopicContentDocument {
  return {
    _id: 'topic',
    roadmapSlug: 'javascript',
    nodeId: 'node',
    description: '# Functions\n\nLearn about JavaScript functions.',
    resources: [],
    createdAt: new Date(0),
    updatedAt: new Date(0),
  };
}

test('preserves every resource through the topic Markdown-to-HTML sync boundary', () => {
  const topic = createTopic();
  topic.resources = allowedOfficialRoadmapTopicResourceType.map(
    (type, index) => ({
      _id: `resource-${index}`,
      type,
      title: `Learn **${type}** with \`examples\``,
      url: `https://example.com/search?type=${type}&q=call)`,
    }),
  );

  const content = prepareOfficialRoadmapTopicContent(topic);
  const root = parse(markdownToHtml(content, false));
  const links = root.querySelectorAll('li > a');

  assert.equal(links.length, topic.resources.length);
  assert.equal(root.querySelector('h1')?.textContent, 'Functions');
  links.forEach((link, index) => {
    const resource = topic.resources[index];
    assert.equal(link.textContent, `@${resource.type}@${resource.title}`);
    assert.equal(link.getAttribute('href'), resource.url);
    assert.equal(link.parentNode.textContent, link.textContent);
  });
});

test('does not change descriptions with no resources', () => {
  const topic = createTopic();
  assert.equal(prepareOfficialRoadmapTopicContent(topic), topic.description);
});
