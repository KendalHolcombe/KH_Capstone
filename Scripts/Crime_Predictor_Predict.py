import numpy as np
import pandas as pd
from Crime_Predictor_Model import *
import pickle


def predictions(user_age, user_sex, user_offense, user_population, user_ratio):

    ## Create user specific test array


    ## Load model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)


    ## Read in input and pre-processing
    df = pd.read_json(json)
    df = Fraud_EDA(df)
    X = df

    ## Predict#
    prediction = model.predict(X)

    return prediction