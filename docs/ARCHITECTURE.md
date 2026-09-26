# Architecture

## Logical layers

1. **Sources:** PostgreSQL transactions, REST product metadata, files, clickstream.
2. **Ingestion:** Airflow schedules batch loads; Kafka carries event streams.
3. **Bronze:** immutable/raw landing on object storage.
4. **Silver:** schema normalization, deduplication, type standardization and SCD2.
5. **Gold:** dimensional facts and customer/product marts.
6. **Analytics:** Snowflake/Synapse and Power BI.

## Reliability controls

- Idempotent business keys
- Watermark + ingestion timestamp separation
- Retryable Airflow tasks
- Schema contracts
- Foreign-key and uniqueness checks
- Freshness checks
- CI tests before merge
