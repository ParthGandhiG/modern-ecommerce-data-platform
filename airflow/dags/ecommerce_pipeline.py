from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
with DAG('ecommerce_data_platform',start_date=datetime(2026,1,1),schedule='@daily',catchup=False,default_args={'retries':2,'retry_delay':timedelta(minutes=5)}) as dag:
    ingest=BashOperator(task_id='generate_ingestion_batch',bash_command='python /opt/project/scripts/generate_data.py')
    quality=BashOperator(task_id='data_quality_gate',bash_command='python /opt/project/quality/checks.py')
    transform=BashOperator(task_id='build_gold',bash_command='python /opt/project/scripts/run_pipeline.py')
    ingest >> quality >> transform
