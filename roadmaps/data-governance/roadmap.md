# Data Governance Roadmap

This roadmap is for data stewards, data and platform engineers moving into governance, data architects, and data leaders. It presents governance as an organizational capability: people make decisions and establish accountability, while processes and technology help those decisions work in practice. Learn the foundations first, then apply them across the data lifecycle and specialize in the areas most relevant to your organization.

## 1. Foundations

Understand the purpose and boundaries of data governance before choosing processes or tools.

### What data governance is

Data governance is the system of decision rights, accountabilities, policies, and oversight that helps an organization manage data as an asset. It sets direction and accountability; data management teams carry out many of the operational practices under that direction.

### Business drivers and outcomes

Connect governance work to concrete outcomes such as trustworthy reporting, reduced operational risk, responsible data use, regulatory obligations, and more efficient data discovery. Define the desired outcome before proposing a committee, policy, or product.

### Data management knowledge areas

Learn how governance relates to data quality, metadata, architecture, security, integration, master data, and lifecycle management. Use a body of knowledge as a map of the discipline, not as a requirement to implement every practice at once.

**Learn more**

- [@official@DAMA International: Data Management Body of Knowledge](https://dama.org/content/body-knowledge)
- [@official@EDM Council: Data Management Capability Assessment Model](https://edmcouncil.org/frameworks/dcam/)

## 2. Operating Model

Set up the people, decision paths, and forums that make governance usable in day-to-day work.

### Governance roles and accountability

Distinguish executive sponsors, data owners, data stewards, custodians, platform teams, and data consumers. Assign accountability to roles with the authority and context to make decisions; stewardship is an ongoing responsibility, not just a committee title.

### Decision rights and escalation

Specify which decisions are made centrally, which belong to a domain, and how conflicts or exceptions are resolved. Document decision owners, required evidence, escalation routes, and how decisions are communicated.

### Centralized, federated, and hybrid models

Compare operating models against the organization's scale, risk, autonomy, and regulatory needs. A hybrid model often sets shared principles centrally while allowing domains to implement them in context; choose a model based on decision needs rather than fashion.

### Councils, working groups, and RACI

Use governance councils for decisions that need cross-functional authority, and working groups for focused implementation. Use a RACI or equivalent responsibility map to expose gaps and overlaps, then keep it aligned with actual work.

**Learn more**

- [@official@EDM Council: DCAM](https://edmcouncil.org/frameworks/dcam/)
- [@article@DAMA International: Data Management Body of Knowledge](https://dama.org/content/body-knowledge)

## 3. Policies, Standards, and Controls

Turn principles and obligations into clear, actionable expectations and oversight.

### Policy lifecycle

Define how policies are proposed, reviewed, approved, communicated, implemented, monitored, and retired. Name an accountable policy owner and review policies when business processes, technology, or obligations change.

### Standards and procedures

Policies state required outcomes; standards define consistent rules, and procedures explain how people perform the work. Make requirements testable and identify where teams can choose among compliant implementations.

### Control design and evidence

Map important requirements to preventive or detective controls, accountable owners, and evidence that shows whether controls operate. Coordinate with risk, compliance, and audit teams so governance controls fit existing assurance processes.

### Exceptions and remediation

Provide a documented route to request a time-bounded exception, assess its risk, approve it at the right level, and track compensating controls and closure. An exception is not a permanent substitute for resolving a known gap.

## 4. Data Quality

Make data fitness-for-purpose measurable and give people a way to resolve quality problems.

### Quality dimensions and critical data

Select dimensions that matter for a use case, such as accuracy, completeness, validity, consistency, uniqueness, and timeliness. Identify critical data elements and define the expected quality with the people who use and own the data.

### Rules, profiling, and monitoring

Profile data to understand its current state, then express quality expectations as measurable rules. Monitor results at appropriate points in data flows and establish thresholds that distinguish actionable problems from normal variation.

### Issue management and root cause

Record quality issues with impact, affected data, an accountable owner, and a resolution target. Trace recurring defects to their source, coordinate fixes across producers and consumers, and verify that remediation improved the agreed measure.

**Learn more**

- [@official@DAMA International: Data Management Body of Knowledge](https://dama.org/content/body-knowledge)
- [@official@Great Expectations documentation](https://docs.greatexpectations.io/)

## 5. Metadata, Catalog, and Lineage

Make data understandable and discoverable by connecting business meaning to technical implementation.

### Business glossary and metadata

Agree on business terms, definitions, owners, and approved usage. Relate those terms to technical metadata such as schemas and columns, and operational metadata such as freshness, quality results, and access history.

### Cataloging and discovery

Help people find and evaluate data by documenting its purpose, source, owner, sensitivity, quality signals, and access process. Establish contribution and review practices so catalog entries remain useful as systems change.

### Lineage and impact analysis

Trace how data is created, transformed, combined, and delivered to consumers. Use lineage to investigate quality incidents, understand downstream impact, support audits, and assess proposed changes; record the limits of automated lineage.

**Learn more**

- [@official@W3C: PROV Overview](https://www.w3.org/TR/prov-overview/)
- [@official@Dublin Core: DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)

## 6. Master and Reference Data

Coordinate shared entities and code sets so important records can be interpreted consistently across systems.

### Master data

Identify core entities such as customers, products, locations, and suppliers, and define ownership, matching rules, survivorship decisions, and authoritative sources. Choose implementation patterns that fit the domain and integration architecture.

### Reference data

Manage shared classifications, code lists, and hierarchies with clear definitions, effective dates, owners, and change processes. Document mappings when different systems use different representations.

### Golden records and synchronization

Understand how consolidated records are created and distributed, including conflict resolution and synchronization with source systems. A "golden record" is a governed view for defined purposes, not necessarily a single universally correct copy.

## 7. Privacy and Regulatory Compliance

Govern personal and regulated data in coordination with privacy, legal, security, and compliance specialists.

### Classification and personal data inventory

Classify information according to its sensitivity and intended use. Identify personal data and its processing context, including purpose, data subjects, recipients, and relevant jurisdictions; keep inventories connected to systems and owners.

### Consent, purpose, and individual rights

Understand how stated purposes, consent where applicable, and rights requests affect collection, use, sharing, and deletion. Work with privacy and legal teams to determine the requirements that apply to each processing activity.

### Retention and regulatory obligations

Translate applicable obligations into approved retention schedules and operational procedures. Account for legal holds, backups, derived data, and deletion evidence; do not treat a general-purpose roadmap as legal advice.

### Regulatory landscape

Learn the basic scope and terminology of frameworks relevant to your organization, such as GDPR, CCPA/CPRA, and HIPAA. Confirm applicability and interpretation with qualified privacy and legal professionals.

**Learn more**

- [@official@EU General Data Protection Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [@official@California Department of Justice: California Consumer Privacy Act](https://oag.ca.gov/privacy/ccpa)
- [@official@U.S. Department of Health and Human Services: HIPAA](https://www.hhs.gov/hipaa/index.html)

## 8. Data Security Governance

Set expectations for protecting data while partnering with security and platform teams on implementation.

### Access governance

Define who may approve access, what evidence is required, how access is reviewed, and how it is removed when roles or purposes change. Align access decisions with data ownership, sensitivity, and least-privilege principles.

### Protection and auditability

Establish requirements for safeguards such as encryption, masking, and controlled environments according to data classification and risk. Define what access and change events must be logged, who reviews them, and how long evidence is retained.

### Shared responsibility and incident response

Clarify the handoffs among data owners, stewards, security operations, and platform teams. Include data governance roles in incident assessment when data use, lineage, quality, or affected stakeholders need to be identified.

**Learn more**

- [@official@NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [@official@NIST SP 800-53 Rev. 5: Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

## 9. Data Lifecycle Management

Govern data from creation through archival and defensible disposal.

### Lifecycle stages and ownership

Map how data is created or collected, used, shared, archived, and disposed of. Assign owners and controls at each stage, including for extracts, replicas, backups, and derived datasets.

### Retention, archival, and disposal

Apply approved schedules to the systems and copies that hold data. Define archival access and integrity expectations, and coordinate deletion with platform owners while accounting for holds, recovery systems, and documented exceptions.

### Change and end-of-life

Include data impact in system acquisition, migration, decommissioning, and vendor exit plans. Confirm that ownership, lineage, retention, access, and disposal responsibilities remain clear during transitions.

**Learn more**

- [@official@U.S. National Archives: Records Management](https://www.archives.gov/records-mgmt)

## 10. Governance for Analytics and AI

Apply data governance to analytical products and AI systems, with additional review for novel or elevated risks.

### Analytics readiness and reproducibility

Assess whether data has clear definitions, known provenance, appropriate quality, permitted use, and stable access for an analytical purpose. Record transformations and assumptions needed to interpret or reproduce results.

### Data contracts and product expectations

Define agreements between data producers and consumers for schemas, meaning, quality expectations, compatibility, ownership, and change notification. Treat contracts as operational agreements that need monitoring and change management.

### AI data governance

Document dataset provenance, collection context, representativeness, limitations, and permitted use for AI development and evaluation. Connect data controls to model risk, human oversight, monitoring, and incident processes; governance of AI systems requires cross-functional expertise.

### Responsible AI checkpoints

Bring privacy, security, legal, domain, and affected-stakeholder perspectives into risk review. Use proportional checkpoints across the lifecycle, from problem framing and data selection through deployment and ongoing monitoring.

**Learn more**

- [@official@NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [@official@OECD AI Principles](https://oecd.ai/en/ai-principles)

## 11. Metrics, Maturity, and Communication

Show whether governance is improving outcomes and communicate progress in terms that matter to stakeholders.

### Measures and key performance indicators

Choose a small set of measures tied to business and risk outcomes, such as critical-data quality trends, ownership coverage, issue resolution, policy exceptions, or time to approve appropriate access. Define measurement methods and owners to avoid vanity metrics.

### Maturity and improvement

Use maturity models to identify capability gaps and sequence improvements, not to pursue a score for its own sake. Reassess after meaningful changes and connect each improvement initiative to a measurable outcome.

### Reporting and adoption

Tailor communication to data practitioners, executives, risk teams, and affected business units. Report decisions, issues, trends, and trade-offs clearly, and provide channels for feedback and practical support.

**Learn more**

- [@official@EDM Council: DCAM](https://edmcouncil.org/frameworks/dcam/)
- [@official@DAMA International: Data Management Body of Knowledge](https://dama.org/content/body-knowledge)

## 12. Tools Landscape

Select tools only after defining the capabilities, workflows, integrations, and operating ownership needed.

### Capability requirements

Compare catalog and glossary management, lineage, quality, policy workflows, access integration, automation, interoperability, usability, and total operating cost. Evaluate fit with existing architecture and how data and metadata can be exported.

### Example platforms

Explore products such as Collibra, Alation, Microsoft Purview, Atlan, Informatica, Unity Catalog, and Apache Atlas. Compare them against organization-specific requirements; the roadmap does not endorse a particular vendor or imply that a platform alone establishes governance.

### Adoption and operating model

Plan for stewardship workflows, integrations, training, metadata curation, and ongoing ownership before rollout. Start with a specific use case, measure adoption and outcomes, and expand based on evidence.

**Explore**

- [@official@Collibra](https://www.collibra.com/)
- [@official@Alation](https://www.alation.com/)
- [@official@Microsoft Purview](https://www.microsoft.com/en-us/security/business/microsoft-purview)
- [@opensource@Apache Atlas](https://atlas.apache.org/)

## 13. Roles and Career Path

Build skills through practical responsibility and choose a progression that matches the organization's needs.

### Stewardship and domain leadership

Data stewards develop domain knowledge, maintain definitions and quality expectations, coordinate issue resolution, and help users apply policies. Strong stewards combine communication and facilitation with enough technical understanding to work across data flows.

### Governance leadership

Governance leads establish operating models, coordinate cross-functional decisions, prioritize capability improvements, and communicate outcomes. They need influence and organizational skills as well as a working understanding of data management and risk.

### Executive data leadership

Heads of Data Governance and Chief Data Officers align data strategy, accountability, investment, and risk with organizational goals. Titles and reporting lines vary; focus on the authority, remit, and outcomes of the role rather than assuming a single career ladder.

### Professional development

Build experience by facilitating decisions, defining measurable policies, improving data quality, and delivering adoption across domains. Consider credentials such as DAMA CDMP or IAPP CIPP/CIPM as structured learning options, not substitutes for experience or jurisdiction-specific advice.

**Learn more**

- [@official@DAMA International: Certified Data Management Professional](https://cdmp.info/)
- [@official@IAPP Certifications](https://iapp.org/certify/)
