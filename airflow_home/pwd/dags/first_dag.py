import datetime import timedelta 

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

def hello_world():
    print("hello world!")


def hello_airflow():
    print("hello airflow!")

default_args = {
    'owner': 'airflow',
    'start_date'; days_age(2),
    'concurrency': 1,
    'retries': 0
}

dag =  DAG("first_dag",
         default_args=default_args,
         schedule_interval=timedelta(days = 1)
         ) 


t1 = PythonOperator(task_id='hello_world',
                               python_callable=hello_world,
                               dag = dag)

t2 = PythonOperator(task_id="hello_airflow",
                                python_callable=hello_airflow,
                                dag = dag)

t1 >> t2
