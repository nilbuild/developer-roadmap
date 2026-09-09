# Change Tracker API

The Change Tracker API is a feature within Entity Framework Core that monitors the state of entities loaded into the application's memory. It automatically detects modifications, additions, and deletions made to objects, keeping track of their current values compared to their original state. This mechanism allows the framework to determine which specific updates need to be synchronized with the database when the SaveChanges method is invoked.

Visit the following resources to learn more:

- [@article@Change Tracking in EF Core](https://learn.microsoft.com/en-us/ef/core/change-tracking/)
- [@article@Intro to Change Tracking](https://www.oreilly.com/library/view/programming-entity-framework/9781449331825/ch05.html)
- [@article@ChangeTracker in Entity Framework Core](https://www.entityframeworktutorial.net/efcore/changetracker-in-ef-core.aspx)