# Observability

Recommended production metrics:

- `pipeline_duration_seconds`
- `records_ingested_total`
- `records_rejected_total`
- `data_quality_pass_rate`
- `source_freshness_seconds`
- `kafka_consumer_lag`
- `spark_failed_tasks_total`
- `gold_table_last_success_timestamp`

Alert examples:

1. Freshness > SLA for two consecutive runs.
2. DQ failure rate > 1%.
3. Record volume deviates > 30% from seven-day baseline.
4. Kafka consumer lag exceeds agreed threshold.
