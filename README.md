# Modern E-Commerce Data Platform

Production-style data engineering portfolio project demonstrating **batch + streaming ingestion, medallion architecture, PySpark, Delta Lake, dbt, Airflow, Kafka, Snowflake-ready SQL, Great Expectations, Terraform/Azure architecture, Docker and CI/CD**.

> **Portfolio note:** This repository is intentionally self-contained. Local components run with Docker/Python and use synthetic data. Azure, Snowflake and Kafka deployment definitions are included as production mappings/templates rather than claiming access to a live employer environment.

## Architecture

```text
 PostgreSQL      REST API       CSV/JSON       Kafka clickstream
     |              |              |                 |
     +--------------+--------------+-----------------+
                            |
                    Airflow / ingestion
                            |
                     Bronze / Delta
                            |
                  PySpark transformations
                            |
                    Silver / Delta
                            |
              Great Expectations + dbt
                            |
                      Gold / marts
                            |
                +-----------+-----------+
                |                       |
            Snowflake                Power BI
          / Synapse-ready          KPI dashboard
```

## Engineering capabilities demonstrated

- Multi-source ingestion and source-to-target mapping
- Batch and streaming architecture
- Bronze/Silver/Gold medallion design
- Delta Lake tables and ACID-oriented processing
- Incremental loads and watermarking
- SCD Type 2 customer history
- Dimensional modeling and semantic-ready marts
- dbt staging/intermediate/mart layers
- dbt tests and source freshness configuration
- Great Expectations-style data quality suite
- Airflow orchestration, retries and dependency management
- Kafka producer/consumer examples
- Snowflake/Synapse-compatible analytical SQL
- Terraform templates for Azure Data Lake, Databricks and supporting resources
- Dockerized local development
- GitHub Actions CI
- Unit tests and pipeline validation
- Observability metrics and failure handling

## Local quick start

```bash
git clone <your-repository-url>
cd modern-ecommerce-data-platform
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_data.py
python scripts/run_pipeline.py
pytest -q
```

Expected output includes Bronze/Silver/Gold record counts and a final `QUALITY_GATE=PASS`.

### Docker

```bash
docker compose up --build
```

Services include PostgreSQL, Kafka, Airflow, and a local project container. Cloud services are not required for the local demo.

## Project structure

```text
src/                     reusable Python/PySpark pipeline code
dbt/                     analytics transformations, tests and snapshots
airflow/                 orchestration DAGs
streaming/               Kafka producer/consumer patterns
quality/                 data quality checks and expectations
infrastructure/terraform Azure infrastructure templates
dashboard/               KPI catalog and Power BI design
schemas/                 source contracts and schema evolution examples
docs/                    architecture, ADRs and operating model
tests/                   automated tests
scripts/                 reproducible data generation and local execution
```

## Data model

### Dimensions
- `dim_customer` — SCD2 customer history
- `dim_product` — product/category attributes
- `dim_date` — calendar attributes

### Facts
- `fact_orders` — order-line grain revenue facts
- `fact_payments` — payment events
- `fact_web_events` — clickstream events

## Production design decisions

### Why Delta Lake?
Delta provides transactional table semantics, schema enforcement/evolution and reliable incremental processing on object storage. The local project keeps the transformations portable; the production mapping targets Azure Data Lake + Databricks.

### Why dbt after Spark?
PySpark handles large-scale engineering transformations and ingestion-oriented processing. dbt owns warehouse-facing analytical transformations, tests, documentation and lineage. This separation mirrors common lakehouse/warehouse operating models.

### Why Kafka?
Clickstream events have different latency requirements from transactional batch data. Kafka decouples event producers from consumers and allows replayable event processing.

### Idempotency
Every pipeline stage is designed around deterministic keys, partition dates and merge semantics. Rerunning a completed batch should not create duplicate business facts.

### Late-arriving data
The design keeps event timestamps separate from ingestion timestamps. Watermarks and partition-aware processing allow late events to be incorporated without rebuilding the entire dataset.

## Cloud mapping

| Local | Production Azure | Warehouse alternative |
|---|---|---|
| Local files | ADLS Gen2 | S3/GCS equivalent |
| PySpark | Azure Databricks | EMR/Dataproc |
| Airflow | Managed Airflow / orchestration | Cloud Composer equivalent |
| Delta | Delta Lake on ADLS | Iceberg/Hudi alternatives |
| PostgreSQL | Azure Database for PostgreSQL | RDS/Cloud SQL |
| dbt | dbt Cloud/Core | dbt Cloud/Core |
| Kafka | Confluent/Azure Event Hubs pattern | MSK/Pub/Sub |
| Gold SQL | Snowflake / Synapse | BigQuery/Redshift |
