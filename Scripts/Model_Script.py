import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_test_split(train_df, test_df):
        y_train = train_df.pop('county').values
        X_train = train_df.values
        y_test = test_df.pop('county').values
        X_test = test_df.values

def build_model(X_train, X_test, y_train, y_test):
    # check that the train and test shapes match

    # build model
    clf = RandomForestClassifier(oob_score=True, n_estimators=500, max_depth=50, max_features='auto')
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    proba_preds = clf.predict_proba(X_test)
    pass