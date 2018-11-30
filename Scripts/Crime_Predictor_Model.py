import numpy as np
import pandas as pd
from Query_Script import Query_to_DF
from Features_Script import feature_engineering
from sklearn.ensemble import RandomForestClassifier
import pickle


class Crime_Model(object):

    def __init__(self, train_query, test_query):
        self.train_query = train_query
        self.test_query = test_query

    def get_data(self):
        '''
        Create dataframes from queries
        Create features set X
        Create targets set y
        '''
        train_df = Query_to_DF(self.train_query, self.test_query)[0]
        y_train = train_df.pop('county').values
        X_train = train_df
        # test_df = Query_to_DF(self.train_query, self.test_query)[1]
        # test_df = test_df.pop('county')
        # X_test = test_df

        return X_train, y_train

    def fit(self, X_train, y_train):
        '''
        Fit Random Forest Classifier with training data
        '''
        self.model = RandomForestClassifier(oob_score=True, n_estimators=50, max_depth=10, min_samples_split=2)

        self.model.fit(X_train, y_train)


    def predict_proba(self, user_data):
        '''
        Returns predicted probabilities for crime to occur in each county
        '''
        return self.model.predict_proba(user_data)


    def predict(self, user_data):
        '''
        Returns predicted county crime occurred in
        '''
        return self.model.predict(user_data)


if __name__ == '__main__':
    data_path = "data/data.json"
    model = Crime_Model(train_query, test_query)
    X_train, y_train = model.get_data()
    model.fit(X_train, y_train)

    with open('model.pkl', 'wb') as f:
        # Write the model to a file.
        pickle.dump(model, f)