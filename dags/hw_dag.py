import datetime as dt
import os
import sys

from airflow.models import DAG
from airflow.operators.python import PythonOperator

# path = "/opt/airflow_hw"
path = os.path.expanduser('~/airflow_hw')

# Add the project code path to the environment variable so it's accessible to the Python process
os.environ['PROJECT_PATH'] = path
# Добавим путь к коду проекта в $PATH, чтобы импортировать функции
sys.path.insert(0, path)

from modules.pipeline import pipeline
from modules.predict import predict



args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2024, 9, 28),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
}

with DAG(
        dag_id='car_price_prediction',
        schedule="00 15 * * *",
        default_args=args,
) as dag:
    pipeline_task = PythonOperator(
        task_id='pipeline',
        python_callable=pipeline,
        dag=dag
    )
    prediction_task = PythonOperator(
        task_id='prediction',
        python_callable=predict,
        dag=dag
    )

    pipeline_task >> prediction_task
