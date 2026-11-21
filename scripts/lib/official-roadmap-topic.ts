export const allowedOfficialRoadmapTopicResourceType = [
  'roadmap',
  'official',
  'opensource',
  'article',
  'course',
  'podcast',
  'video',
  'book',
  'feed',
] as const;
export type AllowedOfficialRoadmapTopicResourceType =
  (typeof allowedOfficialRoadmapTopicResourceType)[number];

export type OfficialRoadmapTopicResource = {
  _id: string;
  type: AllowedOfficialRoadmapTopicResourceType;
  title: string;
  url: string;
};

export interface OfficialRoadmapTopicContentDocument {
  _id: string;
  roadmapSlug: string;
  nodeId: string;
  description: string;
  resources: OfficialRoadmapTopicResource[];
  createdAt: Date;
  updatedAt: Date;
}

export type SyncToDatabaseTopicContent = Omit<
  OfficialRoadmapTopicContentDocument,
  'createdAt' | 'updatedAt' | '_id' | 'resources'
> & {
  resources: Omit<OfficialRoadmapTopicResource, '_id'>[];
};

export function escapeMarkdownLinkText(text: string) {
  return text
    .replace(/\\/g, '\\\\')
    .replace(/</g, '\\<')
    .replace(/>/g, '\\>')
    .replace(/\[/g, '\\[')
    .replace(/\]/g, '\\]');
}

export function formatOfficialRoadmapTopicResourceLink(
  resource: Pick<OfficialRoadmapTopicResource, 'type' | 'title' | 'url'>,
) {
  return `- [@${resource.type}@${escapeMarkdownLinkText(resource.title)}](${resource.url})`;
}

export function prepareOfficialRoadmapTopicContent(
  topic: OfficialRoadmapTopicContentDocument,
) {
  const { description, resources = [] } = topic;

  let content = description;
  if (resources.length > 0) {
    const resourceLinks = resources
      .map(formatOfficialRoadmapTopicResourceLink)
      .join('\n');

    content += `\n\nVisit the following resources to learn more:\n\n${resourceLinks}`;
  }

  return content;
}

/**
 * Picks the heading for a topic description. Uses the `# Heading` from the
 * content file when there is one, and falls back to the node label from the
 * roadmap otherwise, so a file without a heading never produces `# undefined`.
 */
export function resolveTopicHeading(
  heading: string | null | undefined,
  label: string,
): string {
  const fromFile = heading?.trim();
  return fromFile ? fromFile : label.trim();
}

/**
 * Whether a line of plain text is the topic label written without `#`, i.e. a
 * heading that lost its marker. Comparison ignores case and surrounding spaces.
 */
export function isTopicLabelLine(
  text: string | null | undefined,
  label: string,
): boolean {
  const line = text?.trim().toLowerCase();
  return Boolean(line) && line === label.trim().toLowerCase();
}
