# Architecture

```text
Synthetic Source CSVs
        |
        v
Python ingestion / profiling
        |
        v
Staging layer
        |
        v
SQL transformations
        |
        +--------------------+
        |                    |
        v                    v
Dimension models       Fact models
        |                    |
        +---------+----------+
                  |
                  v
        Analytics SQL layer
                  |
                  v
       Forecasting preparation
```

## Layers

### Source
Raw synthetic CSV files under `data/sample/`.

### Staging
Light cleaning and type normalization.

### Transformation
Business rules and joins.

### Models
Fact and dimension tables.

### Analytics
Business-facing KPI queries.

### Validation
Reconciliation and data-quality checks.
