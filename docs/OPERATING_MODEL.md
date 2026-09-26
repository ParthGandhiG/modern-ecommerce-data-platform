# Operating Model

### Freshness
Daily batch SLA: < 30 minutes from source close to gold availability in the demo design.

### Failure handling
Airflow retries transient failures twice. Persistent failures stop downstream transformations and should page/notify the operator in a production deployment.

### Data quality
The quality gate blocks the Gold layer when key constraints fail.

### Observability
Track pipeline duration, records in/out, rejected records, freshness, DQ pass rate and consumer lag.
