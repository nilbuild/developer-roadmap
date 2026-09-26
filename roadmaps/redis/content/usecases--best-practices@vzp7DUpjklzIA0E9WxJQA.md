# Usecases / Best Practices

RDB snapshots are best used when point-in-time backups are needed and some data loss on failure is acceptable. They result in compact files and fast restarts. Best practices include storing snapshots on a separate disk and scheduling them at intervals that balance performance impact with recovery granularity.