# Code First and Migrations in Entity Framework Core

Code First is a development approach where you define your application's data models as C# classes, and Entity Framework Core generates the corresponding database schema from those classes. Migrations serve as a version control system for your database, tracking changes made to your C# models over time. When you modify your classes, you create a migration file that captures the difference between the current state of your code and the previous database structure. These migration files are then applied to the database to ensure the schema remains synchronized with the application code.

Visit the following resources to learn more:

- [@article@What is a Code First Migration?](https://www.entityframeworktutorial.net/code-first/what-is-code-first.aspx)
- [@article@Example for Code First Migrations](https://learn.microsoft.com/en-us/ef/ef6/modeling/code-first/migrations/)
- [@article@Code First Migrations in Entity Framework](https://www.c-sharpcorner.com/UploadFile/26b237/code-first-migrations-in-entity-framework/)