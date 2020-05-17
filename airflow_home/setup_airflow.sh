#!/bin/bash


setup_airflow() {

    python -m venv $1
    source $1/bin/activate
    pip install apache-airflow
    cd $1 
    mkdir airflow_home
    export AIRFLOW_HOME='pwd' airflow_home
    cd airflow_home/
    mkdir dags
    airflow initdb
    touch airflow.cfg unitest.cfg
}

setup_airflow
