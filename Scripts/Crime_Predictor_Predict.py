import numpy as np
import pandas as pd
from Query_Script import Query_to_DF
from Features_Script import feature_engineering
from Crime_Predictor_Model import Crime_Model
from Crime_Predictor_Model import *
import pickle


def predictions(json):

    ## Load model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)


    ## Read in input and pre-processing
    #### sample_path = 'test_script_examples.csv'   ## this was used when we were testing a csv file
    #### df = pd.read_json(sample_path)             ## rather than live data
    df = pd.read_json(json)
    df = Fraud_EDA(df)
    X = df


    ## Handle missing columns
    missing_cols = set(model.columns) - set(X.columns)
    # add a missing column in the test set with default value equal to 0
    for c in missing_cols:
        X[c] = 0
    ## ensure the order of columns in the test set is in the same order as the training set
    X = X[model.columns]


    ## Predict#
    prediction = model.predict(X)


    ## Write prediction to postgresql
    X['prediction'] = pd.DataFrame(prediction) #create pandas dataframe with predictions
    #engine to access the fraud database
    engine = create_engine('postgresql+psycopg2://rcm:galvanize@localhost:5432/fraud')
    #write the pandas dataframe to the predictions table
    X.to_sql('predictions', con=engine, if_exists='replace')
