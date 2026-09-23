# Table layouts

Guidance for choosing and structuring tables within IX experiences.

## When to use

Use a table when users need to scan, compare or act on structured data.

## Guidelines

- Keep comparable information in consistent columns.
- Keep equivalent columns consistent across related tables.
- Put the most important columns first.
- Show only the columns users need by default.
- Keep sorting, filtering and row actions predictable.

For full table guidance, always refer to [Tables and data in Design Basics](../../basics/basics.md#11-tables-and-data).

## Recommended patterns

Use table patterns that match the complexity of the data and the tasks users need to perform. Start with the simplest pattern that supports the required content and interactions, then add controls or responsive behaviour only where needed.

### Standard table

Use a standard table for straightforward datasets that primarily need to be read, scanned or compared.

Keep the structure simple, use clear column headings and avoid adding controls that are not needed. Prioritise the most important information and keep comparable data aligned consistently.

[View standard table](../examples/tables/table-standard.png)

### Data table

Use a data table for larger or more complex datasets that need richer interaction, such as sorting, filtering, pagination, selection or row actions.

Use a standard table when users only need to scan and compare a smaller, simpler set of information.

[View data table](../examples/tables/table-data-table.png)

### Tables with varying widths

Choose a table width based on the amount and complexity of the data rather than applying the same width to every table.

Use a fixed or constrained width for simpler tables with a small number of columns. For example, a table may be limited to around 1024px to keep content compact and easy to scan.

Use a wider or full-width table when there are more columns, longer values or information that benefits from side-by-side comparison. Allow the table to use the available page width before introducing horizontal scrolling.

[View fixed width table](../examples/tables/table-fixed-width.png)<br>
[View full width table](../examples/tables/table-full-width.png)

### Table with row actions

Use row actions when users need to perform actions on individual records, such as viewing, editing or deleting an item.

Keep actions in a consistent position across rows. Show common actions directly where space allows, and place secondary or less frequent actions in an overflow menu.

Avoid using row actions for operations that apply to multiple selected rows.

[View table with row actions](../examples/tables/table-row-actions.png)<br>
[View table with row actions overflow](../examples/tables/table-row-actions-overflow.png)

### Table with filtering

Use filtering when users need to narrow a large or varied dataset to find relevant records.

Place filters close to the table and make active filters easy to identify and remove. Use controls that match the type of data being filtered, and preserve the relationship between filters and the results they affect.

Avoid adding filtering to small datasets where users can find information easily by scanning.

[View table with filtering](../examples/tables/table-filtering.png)

### Tables with empty states

Tables should show an appropriate empty state when no data is available on initial load or when searching or filtering returns no results.

[View table with initial load empty state](../examples/tables/table-empty-state-initial-load.png)<br>
[View table with no results empty state](../examples/tables/table-empty-state-no-results.png)

### Tables with multi-select

Use multi-select when users need to perform the same action on several rows at once.

Provide a selection control at the start of each row and clearly show which rows are selected. Reveal bulk actions only when they are relevant, and make it clear whether selecting all applies to the visible page or the entire dataset.

Avoid multi-select where there are no meaningful bulk actions.

[View table with multi-select](../examples/tables/table-multi-select.png)

### Responsive tables

Adapt tables for smaller screens based on the importance and complexity of the data rather than simply shrinking the desktop layout.

Prioritise essential columns and progressively hide or disclose secondary information where appropriate. Use horizontal scrolling when maintaining the table structure is important, and consider an alternative stacked or detail-based layout when the data cannot be understood comfortably in a narrow table.

Keep important identifiers and row actions accessible as the layout changes.

[View responsive table](../examples/tables/table-responsive.png)

## What to avoid

Avoid table patterns that add unnecessary complexity, reduce readability or make the data harder to use.

### One-size-fits-all tables

Avoid applying the same width, density and interaction model to every table. Simple datasets may work best in a constrained layout, while complex datasets may need more space or different responsive behaviour.

### Overloaded tables

Avoid combining too many columns, controls, row actions, filters and selection options in a single view. Prioritise the information and interactions users need most, and progressively disclose secondary functionality.

### Over-constrained tables

Avoid forcing complex data into a narrow layout when doing so causes excessive wrapping, truncation or cramped controls. Allow the table to use more available width where the content requires it.

### Unnecessarily wide tables

Avoid stretching simple tables across the full page when the content does not benefit from the additional space. A constrained width can improve readability and make relationships between columns easier to understand.

### Desktop tables on small screens

Avoid preserving the desktop table layout unchanged on narrow screens. Prioritise essential information, adapt the interaction model and use horizontal scrolling or an alternative layout where appropriate.
