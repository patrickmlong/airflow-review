# airflow-review
mini-review of Apache Airflow functionality


Quick Airflow command line setup:

    $ python -m venv airflow_play
    $ source airflow_play/bin/activate
    $ pip install apache-airflow
    $ airflow_play/
    $ mkdir airflow_home
    $ export AIRFLOW_HOME='pwd' airflow_home
    $ cd airflow_home/
    $ mkdir dags
    $ airflow initdb
    $ touch airflow.cfg unitest.cfg
    $ airflow webserver
    
From a browser access port http://0.0.0.0:8080/
