from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from Pipelines.Extract.api_connector import APIConnector
from Pipelines.Extract.api_connector import APIConnector    
from Pipelines.Extract.exctract_actual_generation import get_token
from Pipelines.Load.load_actual_generation import load_actual_generations_per_production_type, load_actual_generations_per_unit,load_actual_water_reserves,load_actual_generation_mix_15min_time_scale
from Pipelines.Load.load_generation_forecast import load_generation_forecast
from Pipelines.Load.load_generation_capacities import load_generation_capacities_per_production_type, load_generation_capacities_per_production_unit, load_generation_capacities_cpc 
from Pipelines.Load.load_unavailabilty import load_generation_unavailability,load_network_unavailability,load_other_market_information  
from Pipelines.Extract.date_bootstrap_helper import generate_trimester_table, generate_week_table, generate_year_table, generate_biweekly_table
import os
from airflow.utils.task_group import TaskGroup

def get_api_token():
    api_connector = APIConnector()
    return get_token(api_connector)

default_args = {
    'owner': 'airflow',
    'start_date': "2020-01-01"
}

with DAG(
    'rte_data_pipelines_dag',
    default_args=default_args,
    description='DAG for RTE Data Analysis Pipelines',
    catchup=False
) as dag:

    api_connector = APIConnector()
    token = get_token(api_connector)
    start_date = "2020-01-01"

    load_actual_generations_per_production_type_task = PythonOperator(
        task_id='load_actual_generations_per_production_type',
        python_callable=load_actual_generations_per_production_type,
        op_args=[token, api_connector, start_date]
    )

    load_actual_generations_per_unit_task = PythonOperator(
        task_id='load_actual_generations_per_unit',
        python_callable=load_actual_generations_per_unit,
        op_args=[token, api_connector, start_date]
    )

    load_actual_water_reserves_task = PythonOperator(
        task_id='load_actual_water_reserves',
        python_callable=load_actual_water_reserves,
        op_args=[token, api_connector, start_date]
    )

    load_actual_generation_mix_15min_time_scale_task = PythonOperator(
        task_id='load_actual_generation_mix_15min_time_scale',
        python_callable=load_actual_generation_mix_15min_time_scale,
        op_args=[token, api_connector, start_date]
    )

    load_generation_forecast_task = PythonOperator(
        task_id='load_generation_forecast',
        python_callable=load_generation_forecast,
        op_args=[token, api_connector, start_date]
    )

    load_generation_capacities_per_production_type_task = PythonOperator(
        task_id='load_generation_capacities_per_production_type',
        python_callable=load_generation_capacities_per_production_type,
        op_args=[token, api_connector, start_date]
    )

    load_generation_capacities_per_production_unit_task = PythonOperator(
        task_id='load_generation_capacities_per_production_unit',
        python_callable=load_generation_capacities_per_production_unit,
        op_args=[token, api_connector, start_date]
    )

    load_generation_capacities_cpc_task = PythonOperator(
        task_id='load_generation_capacities_cpc',
        python_callable=load_generation_capacities_cpc,
        op_args=[token, api_connector, start_date]
    )

    load_network_unavailability_task = PythonOperator(
        task_id='load_network_unavailability',
        python_callable=load_network_unavailability,
        op_args=[token, api_connector, start_date]
    )

    load_generation_unavailability_task = PythonOperator(
        task_id='load_generation_unavailability',
        python_callable=load_generation_unavailability,
        op_args=[token, api_connector, start_date]
    )

    load_other_market_information_task = PythonOperator(
        task_id='load_other_market_information',
        python_callable=load_other_market_information,
        op_args=[token, api_connector, start_date]
    )

    with TaskGroup("actual_generation_group") as actual_generation_group:
        load_actual_generations_per_production_type_task
        load_actual_generations_per_unit_task
        load_actual_water_reserves_task
        load_actual_generation_mix_15min_time_scale_task

    with TaskGroup("generation_capacities_group") as generation_capacities_group:
        load_generation_capacities_per_production_type_task
        load_generation_capacities_per_production_unit_task
        load_generation_capacities_cpc_task

    with TaskGroup("unavailability_group") as unavailability_group:
        load_network_unavailability_task
        load_generation_unavailability_task
        load_other_market_information_task

