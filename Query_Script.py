import pandas as pd
import psycopg2
import json


def Query_to_DF(query):
    
    with open('config.json') as f:
        conf = json.load(f)
        host = conf['host']
        database = conf['database']
        user = conf['user']
        passw = conf['passw']

    conn_str = "host={} dbname={} user={} password={}".format(host, database, user, passw)
    conn = psycopg2.connect(conn_str)

    df = pd.read_sql(query, con=conn)
    return df

# if __name__ == '__main__':
#     Query_to_DF()
