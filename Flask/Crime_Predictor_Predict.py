import numpy as np
import pandas as pd
import Crime_Predictor_Model
from Crime_Predictor_Model import Crime_Model
import pickle


def predictions(user_age, user_sex, user_offense, user_population):

    ## Variables
    rural_dict = {'beds_crime': 1.046512, 'beds_pop': 0.011503, 'crime_pop': 0.006680, 'fire_crime': 0.046512,
                  'fire_pop': 0.000511, 'officers': 11.158416, 'civilians': 2.217822}

    suburban_dict = {'beds_crime': 0.151757286949886, 'beds_pop': 0.005646, 'crime_pop': 0.024431701017811704,
                     'fire_crime': 0.0275974039684559, 'fire_pop': 0.000423204273721699, 'officers': 16.167896,
                     'civilians': 7.837446}

    urban_dict = {'beds_crime': 0.129593564474366, 'beds_pop': 0.00717198666494045, 'crime_pop': 0.0342232008026929,
                  'fire_crime': 0.0103548547384775, 'fire_pop': 0.000313079104091144, 'officers': 69.365510,
                  'civilians': 36.503884}

    metro_dict = {'beds_crime': 0.164197312713881, 'beds_pop': 0.00722583648926116, 'crime_pop': 0.0205709011178829,
                  'fire_crime': 0.00696558475377245, 'fire_pop': 0.000157663331486491, 'officers': 207.098791,
                  'civilians': 59.745162}

    predict_dict = {'age_num': 0, 'officers': 1, 'civilians': 2, 'crime_pop_ratio': 3, 'beds_pop_ratio': 4,
    'beds_crime_ratio': 5, 'fire_pop_ratio': 6, 'fire_crime_ratio': 7, 'victim_sex_F': 8, 'victim_sex_M': 9,
    'victim_sex_U': 10, 'Arson': 11, 'Assault Offenses': 12, 'Bribery': 13, 'Burglary/Breaking & Entering': 14,
    'Counterfeiting/Forgery': 15, 'Destruction/Damage/Vandalism of Property': 16, 'Drug/Narcotic Offenses': 17,
    'Embezzlement': 18, 'Extortion/Blackmail': 19, 'Fraud Offenses': 20, 'Homicide Offenses': 21,
    'Human Trafficking': 22, 'Kidnapping/Abduction': 23, 'Larceny/Theft Offenses':24, 'Motor Vehicle Theft': 25,
    'Pornography/Obscene Material': 26, 'Prostitution Offenses': 27, 'Robbery': 28, 'Sex Offenses': 29,
    'Stolen Property Offenses': 30, 'Weapon Law Violations': 31, 'Under 10,000': 32, '10,000 - 99,999': 33,
    '100,000 - 499,999': 34, 'Over 500,000': 35}

    user_test = np.zeros(36)

    ## Create user specific test array
    user_test[0] = user_age
    if user_sex == 'F':
        user_test[8] = 1
    else:
        user_test[9] = 1
    user_test[predict_dict[user_offense]] = 1
    if user_population == 'Under 10,000':
        user_test[1] = rural_dict['officers']
        user_test[2] = rural_dict['civilians']
        user_test[3] = rural_dict['crime_pop']
        user_test[4] = rural_dict['beds_pop']
        user_test[5] = rural_dict['beds_crime']
        user_test[6] = rural_dict['fire_pop']
        user_test[7] = rural_dict['fire_crime']
        user_test[32] = 1
    elif user_population == '10,000 - 99,999':
        user_test[1] = suburban_dict['officers']
        user_test[2] = suburban_dict['civilians']
        user_test[3] = suburban_dict['crime_pop']
        user_test[4] = suburban_dict['beds_pop']
        user_test[5] = suburban_dict['beds_crime']
        user_test[6] = suburban_dict['fire_pop']
        user_test[7] = suburban_dict['fire_crime']
        user_test[33] = 1
    elif user_population == '100,000 - 499,999':
        user_test[1] = urban_dict['officers']
        user_test[2] = urban_dict['civilians']
        user_test[3] = urban_dict['crime_pop']
        user_test[4] = urban_dict['beds_pop']
        user_test[5] = urban_dict['beds_crime']
        user_test[6] = urban_dict['fire_pop']
        user_test[7] = urban_dict['fire_crime']
        user_test[34] = 1
    else:
        user_test[1] = metro_dict['officers']
        user_test[2] = metro_dict['civilians']
        user_test[3] = metro_dict['crime_pop']
        user_test[4] = metro_dict['beds_pop']
        user_test[5] = metro_dict['beds_crime']
        user_test[6] = metro_dict['fire_pop']
        user_test[7] = metro_dict['fire_crime']
        user_test[35] = 1

    user_test = user_test.reshape(1, -1)

    ## Load model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    ## Predict
    pred_probs = model.predict_proba(user_test)
    pred_worst = model.predict(user_test)

    # Get top 10 safest counties
    results_df = pd.DataFrame(pred_probs, columns=model.model.classes_)
    results_df = results_df.T.sort_values(results_df.index[-1], ascending=True).T
    safest = results_df.iloc[:,0:10].T


    return safest, pred_worst



