import pandas as pd
import psycopg2
import json


def Query_to_DF(query):
    ''' Pass string query in and return a dataframe of query results

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

    # Run query and return dataframe
    df = pd.read_sql(query, con=conn)
    return df

# if __name__ == '__main__':
#     Query_to_DF()
