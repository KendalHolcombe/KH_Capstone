import pandas as pd
import psycopg2
import json


def Query_to_DF(train_query, test_query):
    '''

    Pass string query in and return a dataframe of query results

    INPUT: string
    OUTPUT: dataframe

    '''

    # Pull postgres details from config file to make connection
    with open('config.json') as f:
        conf = json.load(f)
        host = conf['host']
        database = conf['database']
        user = conf['user']
        passw = conf['passw']

    # Create postgres connection
    conn_str = "host={} dbname={} user={} password={}".format(host, database, user, passw)
    conn = psycopg2.connect(conn_str)

    # Run queries and return dataframes
    train_df = pd.read_sql(train_query, con=conn)
    test_df = pd.read_sql(test_query, con=conn)

    return train_df, test_df

