import pandas as pd
import numpy as np
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy import text
import time
import datetime
import pyodbc, fsspec, os
import redshift_connector
import boto3, io
import json
import xlsxwriter
from xlsxwriter import Workbook
import socket

def lambda_handler(event, context):

    print('Recon process starting...')

    # Get Credentials from secret manager
    secret_name = os.getenv("secret_name")
    secrets_manager_client = boto3.client('secretmanager')

    try:
        response = secrets_manager_client.get_secret_value(SecretId=secret_name)
    except Exception as e:
        raise e
    else:
        if 'SecretString' in response:
            secret_string = response['SecretString']
            secret_dict = json.loads(secret_string)

            rs_username = secret_dict.get("rs_username")
            rs_password = secret_dict.get("rs_password")

            sql_username = secret_dict.get("sql_username")
            sql_password = secret_dict.get("sql_password")
        else:
            print("Error- secret is not string")

    # DWIT
    sql_server = os.getenv("sql_server")
    sql_database = os.getenv("sql_database")

    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=" + sql_server + ";"
        "DATABASE" + sql_database + ";"
        "UID" + sql_username + ";"
        "PWD" + sql_password + ";"
    )
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    # engine = create_engine(connection_url)

    today = datetime.date.today()

    return None
