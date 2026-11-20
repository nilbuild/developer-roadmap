# LEFT JOIN

A `LEFT JOIN` produces one output row per matching pair. When a left row has no match, it contributes one row with `NULL` in the right table's columns. When grouping customers by ID after joining their orders, a customer with no orders has `COUNT(*) = 1` and `COUNT(orders.id) = 0` if order IDs are non-null. The first counts the joined row. The second counts only non-null order IDs.

Visit the following resources to learn more:

- [@article@Practice counting matches after a LEFT JOIN](https://hiredin60.com/lessons/165/?utm_source=roadmapsh&utm_medium=resource&utm_campaign=sql-left-join-practice#sql-left-join-practice)
- [@video@SQL LEFT JOIN - SQL Tutorial](https://www.youtube.com/watch?v=giKwmtsz1U8)