import numpy as np
from Crime_Predictor_Model import Crime_Model
import pickle


def predictions(user_age, user_sex, user_offense, user_population):

    ## Variables
    rural_dict = {'beds_crime': 1.0465116279069768, 'beds_pop': 0.011503067484662576, 'crime_pop': 0.003339903635567236,
                  'fire_crime': 0.04918032786885246, 'fire_pop': 0.0005112474437627812, 'officers': 11.158416,
                  'civilians': 2.217822}

    suburban_dict = {'beds_crime': 0.7780734560797852, 'beds_pop': 0.005645964795748921, 'crime_pop': 0.0288608435735636,
                     'fire_crime': 0.17011891062523973, 'fire_pop': 0.0004335933966854009, 'officers': 16.167896,
                     'civilians': 7.837446}

    urban_dict = {'beds_crime': 0.36263914090106647, 'beds_pop': 0.007158590625022616, 'crime_pop': 0.023604314269714897,
                  'fire_crime': 0.026509040747660376, 'fire_pop': 0.00031802378474501665, 'officers': 69.365510,
                  'civilians': 36.503884}

    metro_dict = {'beds_crime': 208.19382486575793, 'beds_pop': 0.00722454368291119, 'crime_pop': 0.01528558395906832,
                  'fire_crime': 3.3349446614583336, 'fire_pop': 0.0001755805639960661, 'officers': 207.098791,
                  'civilians': 59.745162}

    predict_dict = {'age_num': 0, 'officers': 1, 'civilians': 2, 'crime_pop_ratio': 3, 'beds_pop_ratio': 4,
    'beds_crime_ratio': 5, 'fire_pop_ratio': 6, 'fire_crime_ratio': 7, 'victim_sex_F': 8, 'victim_sex_M': 9,
    'victim_sex_U': 10, 'Arson': 11, 'Assault Offenses': 12, 'Bribery': 13, 'Burglary/Breaking & Entering': 14,
    'Counterfeiting/Forgery': 15, 'Destruction/Damage/Vandalism of Property': 16, 'Drug/Narcotic Offenses': 17,
    'Embezzlement': 18, 'Extortion/Blackmail': 19, 'Fraud Offenses': 20, 'Homicide Offenses': 21,
    'Human Trafficking': 22, 'Kidnapping/Abduction': 23, 'Larceny/Theft Offenses':24, 'Motor Vehicle Theft': 25,
    'Pornography/Obscene Material': 26, 'Prostitution Offenses': 27, 'Robbery': 28, 'Sex Offenses': 29,
    'Stolen Property Offenses': 30, 'Weapon Law Violations': 31, 'Under 25,000': 32, '25,000 - 99,999': 33,
    '100,000 - 499,999': 34, 'Over 500,000': 35}

    user_test = np.zeros(36)

    ## Create user specific test array
    user_test[0] = user_age
    if user_sex == 'F':
        user_test[8] = 1
    else:
        user_test[9] = 1
    user_test[predict_dict[user_offense]] = 1
    if user_population == 'Under 25,000':
        user_test[1] = rural_dict['officers']
        user_test[2] = rural_dict['civilians']
        user_test[3] = rural_dict['crime_pop']
        user_test[4] = rural_dict['beds_pop']
        user_test[5] = rural_dict['beds_crime']
        user_test[6] = rural_dict['fire_pop']
        user_test[7] = rural_dict['fire_crime']
        user_test[32] = 1
    elif user_population == '25,000 - 99,999':
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

    return pred_probs, pred_worst
