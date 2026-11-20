---
name: developer-roadmap-content
description: Write, improve, audit and contribute topic content for the roadmap.sh developer-roadmap repo (nilbuild/developer-roadmap, formerly kamranahmedse), where every roadmap node is a markdown file at roadmaps/ROADMAP/content/TOPIC-SLUG@NODE-ID.md with a title, a short paragraph and typed resource links like [@article@...]. Use this skill whenever the user is working in a developer-roadmap checkout or mentions roadmap.sh topics, roadmap content files, node IDs, "@official@"/"@video@" link tags, thin or empty topic descriptions, adding or vetting learning resources for a roadmap, linting or checking a roadmap's content folder, finding topics that have no file yet, or preparing a content PR for roadmap.sh, even if they don't name the repo.
---

# developer-roadmap topic content

roadmap.sh shows a popup for each node on a roadmap. The popup's text comes from one markdown file per node in this repo. A GitHub Action (`scripts/sync-repo-to-database.ts`) parses changed files and posts them to roadmap.sh, so a file that is malformed doesn't fail loudly. It just shows up wrong on the site. Most of this skill exists to keep that from happening.

The repo holds content only. There is no app to run and no roadmap JSON on disk. Node IDs live in roadmap.sh's database.

## Repo facts

- Topic files: `roadmaps/<roadmap-slug>/content/<topic-slug>@<node-id>.md`. The node ID links a file to its node. The slug is only for humans. When you edit a file, never change the `@<node-id>` part.
- The slug for a new file is the node label slugified exactly like `scripts/lib/slugger.ts`: lowercase, drop everything except letters, digits, `_`, `-` and spaces, trim, then turn spaces into `-`. "How does the internet work?" becomes `how-does-the-internet-work`. A label like `$?` gives an empty slug, so `@hxjqlxolS_ahtro4T0EKG.md` is a valid name.
- Files like `index.md` or names with no `@` are not topics. The sync skips them, so leave them alone.
- Existing files end without a trailing newline (that's what the sync writes). Keep whatever ending a file already has, so the diff shows only your change.

## The checker script

`scripts/check_content.py` is next to this file. It needs Python 3 and nothing else. Run it from the repo root:

```bash
python3 <skill-dir>/scripts/check_content.py lint roadmaps/frontend            # one roadmap
python3 <skill-dir>/scripts/check_content.py lint roadmaps/frontend/content/x@id.md
python3 <skill-dir>/scripts/check_content.py lint roadmaps --errors-only       # whole repo (~11k files, a few seconds)
python3 <skill-dir>/scripts/check_content.py lint roadmaps/sql --json           # machine-readable
python3 <skill-dir>/scripts/check_content.py nodes frontend                     # live node list from roadmap.sh
python3 <skill-dir>/scripts/check_content.py nodes frontend --status missing    # nodes with no file yet
python3 <skill-dir>/scripts/check_content.py nodes frontend --status stale      # renamed, duplicate or orphaned files
python3 <skill-dir>/scripts/check_content.py fix-order roadmaps/frontend --dry-run  # preview link reordering
python3 <skill-dir>/scripts/check_content.py fix-order roadmaps/frontend        # apply it
```

`fix-order` only reorders link lines into the allowed type order. It's a stable sort, so links of the same type keep their order. It changes no text, URL or whitespace. It skips files with malformed links or unknown types, which need a human decision. Use it instead of reordering links by hand: it's exact, and the diff stays reviewable.

`lint` is offline. It checks every rule in the format section below. It exits 1 if it finds any error, so you can use it as a gate.

`nodes` fetches `https://roadmap.sh/api/v1-official-roadmap/<slug>`, a public endpoint that needs no auth. For each topic node it prints the node ID, its label, the filename the node should have, and whether that file exists. Use it whenever you need a node ID or a correct filename. Don't guess either: a wrong ID means the sync can't find the node and drops the file.

The repo already has errors: a few hundred link-order problems and a handful of others. Lint before you edit, so you can tell the user which problems you found and which you introduced. Your own changes should lint clean.

## File format

```markdown
# Topic Title

One paragraph that explains the topic.

Visit the following resources to learn more:

- [@official@Exact Page Title](https://...)
- [@article@Exact Page Title](https://...)
- [@video@Exact Video Title](https://www.youtube.com/watch?v=...)
```

How the sync reads a file, and why each rule matters:

- The **`# Title`** must be the first line, and there should be only one. The sync uses it as the popup heading.
- **Description.** Everything between the title and the links is shown as the description.
- **The visit line** must read exactly `Visit the following resources to learn more:`, followed by a blank line. When a file has links, the sync deletes the last paragraph before them on the assumption that it's this line. If you leave it out or reword it, real description text disappears from the site.
- **One unbroken list.** The sync keeps only the last list made entirely of links. A blank line inside the list splits it into two, and everything above the split is lost. Nothing may follow the list.
- **Link syntax** is `- [@type@Title](url)`. The allowed types, in the order links must appear, are: `roadmap` > `official` > `opensource` > `article` > `course` > `podcast` > `video` > `book` > `feed`. An unknown type such as `@docs@` or `@blog@` is silently filed as an article. `@roadmap@` links point to another roadmap.sh roadmap, for example `[@roadmap@Visit the Dedicated Linux Roadmap](https://roadmap.sh/linux)`.
- **Repo rules** from `contributing.md`: content must be in English, a topic has at most **8 links**, **no geeksforgeeks.org** links, and no links to your own blog or other self-promotion.
- **Brackets in titles.** If a link title contains `[` `]` `<` or `>`, escape them with a backslash. This is what the repo's own formatter does.

## Writing or improving a topic

1. **Find the file and node.** If the file exists, read it first. If it doesn't, get the node ID and the correct filename from `nodes <roadmap> --status missing`. Read two or three neighbouring topics in the same roadmap too: they show the roadmap's voice, how deep it goes, and which links it already uses, so you don't repeat a resource the next topic already covers.
2. **Write the description for this roadmap's learner.** It should be one paragraph, usually 40–90 words; the repo's median is about 57. Say what the thing is, then why it matters or when you'd use it in the context of this roadmap. A "Caching" topic reads differently on the backend roadmap than on the frontend one. Keep it plain and factual:
   - No "In this section we will…".
   - No marketing words ("powerful", "seamless", "revolutionary").
   - No first person.
   - No bullet lists or code blocks unless the topic truly needs them.
   - The maintainers reject rewrites that "don't add any value", so when improving a topic, change it only if the result is clearly better: more accurate, clearer, or filling a gap.
3. **Choose 2–6 resources. Quality beats count, and 8 is a hard limit.**
   - **Official documentation first.** Then a solid free article or tutorial, then a good video if one exists.
   - **Prefer current, stable, free sources:** vendor docs, MDN, the project's GitHub repo, well-known engineering blogs, and freeCodeCamp or YouTube channels that are still maintained.
   - **Avoid** content farms, paywalled or login-walled pages, very old material for fast-moving topics, and anything on a banned domain.
   - **Verify every URL before you put it in the file.** Fetch it and check that it loads, that it's the page you think it is, and that the title you write matches the page's real title. Made-up or slightly-wrong URLs are the most common way generated content gets rejected. If you can't fetch the page, don't add the link. Tell the user instead.
   - **Keep the links that are already there** unless they're dead, off-topic, banned, or over the limit. Say which ones you removed and why.
4. **Format, then lint.** Run `lint` on each file you touched and fix anything it reports.
5. **Report back.** Give the path of each file you changed, a short before/after of the description, the links you added or removed, and any URL you couldn't verify.

When you're asked to fill many topics, such as every thin topic in a roadmap, first list the targets with `lint roadmaps/<slug> --json`. Look for the `thin-description` and `no-description` codes, and for `no-links` notes on topics that clearly should have resources. Show the user the list and agree on the scope, then work through it one topic at a time. Verifying links is the slow part, and it's still worth doing.

## Auditing content

1. Run `lint` on the scope the user asked about: one file, one roadmap, or the whole `roadmaps/` folder.
2. Summarise the results by issue code, with counts. Lead with the issues that change what roadmap.sh actually shows:
   - `visit-line`: description text gets dropped.
   - `structure`: links get lost.
   - `link-type`: links get the wrong category.
   - `duplicate-node` and `filename`: the wrong file or no file gets synced.
   - `title` and `no-description`.

   After those come rule violations: `link-count`, `banned-domain`, `link-order`, `duplicate-link`. Then the soft ones: `thin-description`, `http://` links, and topics with no links. `link-order` is the most common error in the repo, but it's a style-guide issue only: the sync re-sorts links before saving, so the order doesn't change what the site shows. Say that, so the user doesn't think hundreds of topics are broken.
3. List the worst files with paths so the user can click through, rather than pasting the whole report.
4. If the audit is about a roadmap, also run `nodes <slug>`:
   - `missing` means a node has no content file yet.
   - `renamed` means the slug is out of date with the label.
   - `duplicate` means two files share one node ID. Keep the one whose name matches the expected filename.
   - `stale` means the node no longer exists on the roadmap.

   Renames and deletions of stale files are normally handled by the maintainers' `cleanup-orphaned-content` workflow. Point them out rather than fixing them yourself, unless the user asks.
5. Before renaming a file to fix its name, check whether the target name already exists. A stray copy such as `x@id.md.md` sitting next to `x@id.md` is a leftover, not a file to rename over the real one. Compare the two, then propose deleting the stray. If it has a resource worth keeping, suggest moving that link into the real file.
6. Fix things only when the user wants fixes. Mechanical fixes are safe to batch once agreed: reordering links, correcting the visit line, removing blank lines inside the list, or renaming an unknown type to the right one. Content judgement calls, such as which link to drop when a topic is over 8, should be shown to the user first.

## Preparing a contribution PR

contributing.md asks for one PR for content additions, a meaningful commit message, and a PR with a real description, not the default title. It also asks contributors to look at existing issues and PRs first.

1. Check for open PRs that touch the same topics: `gh pr list --repo nilbuild/developer-roadmap --search "<roadmap or topic>" --state open`.
2. Work on a branch, never on `master`: `git switch -c content/<roadmap>-<short-topic>`.
3. Lint every changed file. `git diff --name-only | grep '/content/'` lists them. Every changed file must lint clean.
4. Write the commit message in the repo's style, a lowercase conventional prefix with a clear summary. For example: `docs(frontend): expand the SvelteKit and Astro topic descriptions`.
5. The PR title should say what changed and in which roadmap. The body should cover:
   - which topics changed, and why: thin, outdated, missing or broken links;
   - each new resource, and why it's worth including (contributing.md asks contributors to argue for each one);
   - confirmation that the files follow the style guide and that the links were checked.
6. **Only commit, push or open the PR when the user says to.** Most contributors can't push to `nilbuild/developer-roadmap` directly. If `git push` is refused, offer to fork with `gh repo fork --remote` and push the branch to the fork. A shallow clone (`--depth 1`) is fine for this.
