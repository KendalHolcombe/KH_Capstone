from Query_Script import Query_to_DF
from Features_Script import feature_engineering
from sklearn.ensemble import RandomForestClassifier
import pickle


class Crime_Model(object):

    def __init__(self, train_query):
        self.train_query = train_query

    def get_data(self):
        '''
        Create dataframes from queries
        '''
        train_df = Query_to_DF(self.train_query)

        return train_df

    def clean_data(self, train_df):
        '''
        Create features set X
        Create targets set y
        '''
        train_df = feature_engineering(train_df)
        y_train = train_df.pop('county').values
        X_train = train_df

        return X_train, y_train

    def fit(self, X_train, y_train):
        '''
        Fit Random Forest Classifier with training data
        '''
        self.model = RandomForestClassifier(n_estimators=50, max_depth=10, min_samples_split=2)

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
    train_query = '''
    SELECT      DISTINCT inc.incident_id AS INCIDENT_ID,
                date_part('year',inc.incident_date) AS YEAR,
                vic.age_num,
                vic.sex_code AS VICTIM_SEX,
                LTRIM(RTRIM(oft.offense_name)) AS OFFENSE,
                LTRIM(RTRIM(oft.offense_category_name)) AS OFFENSE_CATEGORY,
                LTRIM(RTRIM(ori.countyname)) AS COUNTY,
                ags.total_officers AS OFFICERS,
                ags.total_civilians AS CIVILIANS

    FROM        nibrs_victim as vic
    JOIN        nibrs_offense as off
    ON          off.incident_id = vic.incident_id
    JOIN        nibrs_offense_type as oft
    ON          oft.offense_type_id = off.offense_type_id
    JOIN        nibrs_incident as inc
    ON          inc.incident_id = vic.incident_id
    JOIN        cde_agencies as ags
    ON          ags.agency_id = inc.agency_id
    JOIN        ori_to_fips as ori
    ON          ori.ori9 = ags.ori

    WHERE       vic.victim_type_id = 4
    AND         inc.incident_date BETWEEN '2014-01-01' AND '2015-12-31';
    '''

    model = Crime_Model(train_query)
    train_df = model.get_data()
    X_train, y_train = model.clean_data(train_df)
    model.fit(X_train, y_train)

    with open('model.pkl', 'wb') as f:
        # Write the model to a file.
        pickle.dump(model, f)