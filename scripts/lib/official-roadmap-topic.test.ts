import assert from 'node:assert/strict';
import { test } from 'node:test';
import {
  isTopicLabelLine,
  resolveTopicHeading,
} from './official-roadmap-topic';

test('uses the heading from the content file when present', () => {
  assert.equal(
    resolveTopicHeading('Template Tags', 'Template Tags'),
    'Template Tags',
  );
  assert.equal(resolveTopicHeading('  Custom Title ', 'Label'), 'Custom Title');
});

test('falls back to the node label instead of "undefined"', () => {
  assert.equal(
    resolveTopicHeading(undefined, 'Networking Fundamentals'),
    'Networking Fundamentals',
  );
  assert.equal(resolveTopicHeading(null, 'OIDC'), 'OIDC');
  assert.equal(resolveTopicHeading('   ', 'Outliers'), 'Outliers');
});

test('keeps topics whose real label is "undefined"', () => {
  assert.equal(resolveTopicHeading('undefined', 'undefined'), 'undefined');
});

test('detects a heading line that lost its "#" marker', () => {
  assert.equal(
    isTopicLabelLine('Networking Fundamentals', 'Networking Fundamentals'),
    true,
  );
  assert.equal(
    isTopicLabelLine('  networking fundamentals ', 'Networking Fundamentals'),
    true,
  );
  assert.equal(
    isTopicLabelLine(
      'Networking fundamentals cover how data moves.',
      'Networking Fundamentals',
    ),
    false,
  );
  assert.equal(isTopicLabelLine(undefined, 'OIDC'), false);
  assert.equal(isTopicLabelLine('', ''), false);
});
