# PostgreSQL Anonymizer

PostgreSQL Anonymizer is an extension that masks or replaces personally identifiable information and other sensitive data inside a PostgreSQL database. Masking rules are declared directly in the database schema with SQL, so the people who know the data model can define which columns are sensitive and how they should be hidden. The extension provides several strategies: static masking, which permanently replaces data in place; dynamic masking, which hides data only from specific roles; and anonymous dumps, which export a masked copy of the database. Masking functions include generating fake but realistic values, partial scrambling, adding noise, and generalization, making it useful for creating safe copies of production data for development, testing, and analytics.

Visit the following resources to learn more:

- [@official@PostgreSQL Anonymizer Website](https://postgresql-anonymizer.readthedocs.io/en/stable/)
- [@opensource@dalibo/postgresql_anonymizer](https://github.com/dalibo/postgresql_anonymizer)