import pandas as pd

def feature_engineering(train_df, test_df):
    '''

    Take in query output dataframe, clean data, and complete feature engineering

    INPUT: dataframe, dataframe
    OUTPUT: dataframe, dataframe

    '''

    ### TRAIN_DF ###
    # Drop NA in victim age column (<2%)
    train_df.dropna(axis=0, subset=['age_num'], inplace=True)

    # Drop NA in hospital_cnt column (<2%)
    train_df.dropna(axis=0, subset=['hosp_cnt'], inplace=True)

    # Drop NA in population column (<2%)
    train_df.dropna(axis=0, subset=['population'], inplace=True)

    # Create Ratio Columns
    train_df['crime_pop_ratio'] = train_df['crime_cnt'] / train_df['population']
    train_df['beds_pop_ratio'] = train_df['bed_cnt'] / train_df['population']
    train_df['beds_crime_ratio'] = train_df['bed_cnt'] / train_df['crime_cnt']
    train_df['fire_pop_ratio'] = train_df['fire_cnt'] / train_df['population']
    train_df['fire_crime_ratio'] = train_df['fire_cnt'] / train_df['crime_cnt']

    # Reduce df to only desired features to train/test model
    train_df = train_df[['age_num', 'victim_sex', 'offense_category', 'location_id', 'population_description',
                         'officers', 'civilians', 'crime_pop_ratio', 'beds_pop_ratio', 'beds_crime_ratio',
                         'fire_pop_ratio', 'fire_crime_ratio', 'county']]

    # Dummize features
    train_df = pd.get_dummies(train_df, columns=['victim_sex', 'offense_category', 'location_id', 'population_description'])


    ### TEST_DF ###
    # Drop NA in victim age column (<2%)
    test_df.dropna(axis=0, subset=['age_num'], inplace=True)

    # Drop NA in hospital_cnt column (<2%)
    test_df.dropna(axis=0, subset=['hosp_cnt'], inplace=True)

    # Drop NA in population column (<2%)
    test_df.dropna(axis=0, subset=['population'], inplace=True)

    # Create Ratio Columns
    test_df['crime_pop_ratio'] = test_df['crime_cnt'] / test_df['population']
    test_df['beds_pop_ratio'] = test_df['bed_cnt'] / test_df['population']
    test_df['beds_crime_ratio'] = test_df['bed_cnt'] / test_df['crime_cnt']
    test_df['fire_pop_ratio'] = test_df['fire_cnt'] / test_df['population']
    test_df['fire_crime_ratio'] = test_df['fire_cnt'] / test_df['crime_cnt']

    # Reduce df to only desired features to train/test model
    test_df = test_df[['age_num', 'victim_sex', 'offense_category', 'location_id', 'population_description',
                       'officers', 'civilians', 'crime_pop_ratio', 'beds_pop_ratio', 'beds_crime_ratio',
                       'fire_pop_ratio', 'fire_crime_ratio', 'county']]

    # Dummyize features
    test_df = pd.get_dummies(test_df, columns=['victim_sex', 'offense_category', 'location_id', 'population_description'])


    # # Ensure features match across train and test dataframes
    # # if this is a prediction make sure DF has same columns as origional used in fitting the model
    # if predict:
    #     # Get missing columns in the training test
    #     missing_cols = set(self.train_cols) - set(X_feat.columns)
    #     # Add a missing column in test set with default value equal to 0
    #     for c in missing_cols:
    #         X_feat[c] = 0
    #     # Ensure the order of column in the test set is in the same order than in train set
    #     X_feat = X_feat[self.train_cols]


    return train_df, test_df