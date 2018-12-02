import pandas as pd

def feature_engineering(train_df):
    '''

    Take in query output dataframe, clean data, and complete feature engineering

    INPUT: dataframe, dataframe
    OUTPUT: dataframe, dataframe

    '''

    ### TRAIN_DF ###

    # Collect metadata
    h_df = pd.read_csv('hosp_query.csv')
    f_df = pd.read_csv('fire_query.csv')
    pop_df = pd.read_csv('census_population.csv')

    ## Add metadata to train_df
    # Crime Count by county
    tmp_df = train_df.groupby(['county']).incident_id.agg('count')
    tmp_df = tmp_df.to_frame().reset_index()
    tmp_df = tmp_df.rename({'incident_id': 'crime_cnt'}, axis='columns')
    train_df = train_df.join(tmp_df.set_index('county'), on='county')
    # Hospital Count by county
    tmp_df2 = h_df.groupby(['county']).hosp_id.agg('count')
    tmp_df2 = tmp_df2.to_frame().reset_index()
    tmp_df2 = tmp_df2.rename({'hosp_id': 'hosp_cnt'}, axis='columns')
    # Total Bed Count by county
    h_df['beds'] = h_df['beds'].clip_lower(1)
    tmp_df3 = h_df.groupby(['county']).beds.agg('sum')
    tmp_df3 = tmp_df3.to_frame().reset_index()
    tmp_df3 = tmp_df3.rename({'beds': 'bed_cnt'}, axis='columns')
    h_df = tmp_df2.join(tmp_df3.set_index('county'), on='county')
    # Fire Station Count by county
    tmp_df4 = f_df.groupby(['county']).fire_id.agg('count')
    tmp_df4 = tmp_df4.to_frame().reset_index()
    tmp_df4 = tmp_df4.rename({'fire_id': 'fire_cnt'}, axis='columns')
    hf_df = tmp_df4.join(h_df.set_index('county'), on='county')
    # Join to train_df
    train_df = train_df.join(hf_df.set_index('county'), on='county')
    # Bring in census populations
    pop_df['county'] = pop_df['county'].str.upper()
    train_df = pd.merge(train_df, pop_df, how='outer', on=['county', 'year'])
    train_df['population_description'] = pd.cut(train_df['population'], [0, 10000, 100000, 500000, 10000000],
                                                labels=['Under 10,000', '10,000 - 99,999', '100,000 - 499,999',
                                                        'Over 500,000'])


    # Drop NA in incident id column (<2%)
    train_df.dropna(axis=0, subset=['incident_id'], inplace=True)

    # Drop NA in victim age column (<2%)
    train_df.dropna(axis=0, subset=['age_num'], inplace=True)

    # Drop NA in hospital_cnt column (<2%)
    train_df.dropna(axis=0, subset=['hosp_cnt'], inplace=True)

    # Drop NA in population column (<2%)
    train_df.dropna(axis=0, subset=['population'], inplace=True)

    # Drop Gambling Offenses from Offense_Category column (only ONE incident across entire dataframe)
    train_df = train_df[train_df.offense_category != 'Gambling Offenses']

    # Create Ratio Columns
    train_df['crime_pop_ratio'] = train_df['crime_cnt'] / train_df['population']
    train_df['beds_pop_ratio'] = train_df['bed_cnt'] / train_df['population']
    train_df['beds_crime_ratio'] = train_df['bed_cnt'] / train_df['crime_cnt']
    train_df['fire_pop_ratio'] = train_df['fire_cnt'] / train_df['population']
    train_df['fire_crime_ratio'] = train_df['fire_cnt'] / train_df['crime_cnt']

    # Reduce df to only desired features to train/test model
    train_df = train_df[['age_num', 'victim_sex', 'offense_category', 'population_description',
                         'officers', 'civilians', 'crime_pop_ratio', 'beds_pop_ratio', 'beds_crime_ratio',
                         'fire_pop_ratio', 'fire_crime_ratio', 'county']]

    # Dummize features
    train_df = pd.get_dummies(train_df, columns=['victim_sex', 'offense_category', 'population_description'])

    return train_df