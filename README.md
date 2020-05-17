# airflow-review
mini-review of Apache Airflow functionality


Quick Airflow command line setup:

    $ python -m venv airflow_play
    $ source airflow_play/bin/activate
    $ pip install apache-airflow
    $ cd airflow_play/
    $ mkdir airflow_home
    $ export AIRFLOW_HOME='pwd' airflow_home
    $ cd airflow_home/
    $ mkdir dags
    $ airflow initdb
    $ airflow webserver
    
From a browser open port http://0.0.0.0:8080/

Or to simply setup an airflow directory:

    $ bash setup_airflow.sh <parent dir>
