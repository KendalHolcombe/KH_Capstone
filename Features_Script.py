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

    # Get crime count by county
    crime_df = train_df.groupby(['county']).incident_id.agg('count')
    crime_df = crime_df.to_frame().reset_index()
    crime_df = crime_df.rename({'incident_id': 'crime_cnt'}, axis='columns')
    train_df.join(crime_df.set_index('county'), on='county')

    # Clean up count columns
    train_df['beds'] = train_df['beds'].clip_lower(0)

    # Create Ratio Columns
    train_df['crime_pop_ratio'] = train_df['crime_cnt'] / train_df['population']
    train_df['beds_pop_ratio'] = train_df['bed_cnt'] / train_df['population']
    train_df['beds_crime_ratio'] = train_df['bed_cnt'] / train_df['crime_cnt']
    train_df['fire_pop_ratio'] = train_df['fire_cnt'] / train_df['population']
    train_df['fire_crime_ratio'] = train_df['fire_cnt'] / train_df['crime_cnt']

    # Reduce df to only desired features to train/test model
    train_df = train_df[['age_num', 'victim_sex', 'offense_category', 'location_id', 'POPULATION_DESCRIPTION',
                         'officers', 'civilians', 'crime_pop_ratio', 'beds_pop_ratio', 'beds_crime_ratio',
                         'fire_pop_ratio', 'fire_crime_ratio', 'county']]

    # Dummize features
    train_df = pd.get_dummies(train_df, columns=['victim_sex', 'offense_category', 'location_id', 'POPULATION_DESCRIPTION'])


    ### TEST_DF ###
    # Drop NA in victim age column (<2%)
    test_df.dropna(axis=0, subset=['age_num'], inplace=True)

    # Get crime count by county
    crime_df = test_df.groupby(['county']).incident_id.agg('count')
    crime_df = crime_df.to_frame().reset_index()
    crime_df = crime_df.rename({'incident_id': 'crime_cnt'}, axis='columns')
    test_df.join(crime_df.set_index('county'), on='county')

    # Clean up count columns
    test_df['beds'] = test_df['beds'].clip_lower(0)

    # Create Ratio Columns
    test_df['crime_pop_ratio'] = test_df['crime_cnt'] / test_df['population']
    test_df['beds_pop_ratio'] = test_df['bed_cnt'] / test_df['population']
    test_df['beds_crime_ratio'] = test_df['bed_cnt'] / test_df['crime_cnt']
    test_df['fire_pop_ratio'] = test_df['fire_cnt'] / test_df['population']
    test_df['fire_crime_ratio'] = test_df['fire_cnt'] / test_df['crime_cnt']

    # Reduce df to only desired features to train/test model
    test_df = test_df[['age_num', 'victim_sex', 'offense_category', 'location_id', 'POPULATION_DESCRIPTION',
                       'officers', 'civilians', 'crime_pop_ratio', 'beds_pop_ratio', 'beds_crime_ratio',
                       'fire_pop_ratio', 'fire_crime_ratio', 'county']]

    # Dummize features
    test_df = pd.get_dummies(test_df, columns=['victim_sex', 'offense_category', 'location_id', 'POPULATION_DESCRIPTION'])


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