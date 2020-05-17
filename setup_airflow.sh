#!/bin/bash


setup_airflow() {

    mkdir $@_dir
    cd $@_dir; pwd;
    mkdir airflow_home
    export AIRFLOW_HOME='pwd' airflow_home
    cd airflow_home/
    mkdir dags
    airflow initdb
    touch airflow.cfg unitest.cfg
}

setup_airflow $@
