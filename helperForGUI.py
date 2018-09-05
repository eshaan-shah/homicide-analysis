'''
Authors: Eshaan Shah, Anindo Saha, Rohit Mudaliar
This py file is helper for the GUI.py
'''

from sklearn.externals import joblib

sex = {
    0: 'Male',
    1: 'Female'
}

age = {
    0: "1-10",
    1: "11-20",
    2: "21-30",
    3: "31-40",
    4: "41-50",
    5: "51-60",
    6: "61-70",
    7: "71-80",
    8: "81-90",
    9: "90+"
}

def makePrediction(selSex, selAge, selRelation, selWeapon):
    '''
    Predicts the class of provided instance
    :param selSex: victim sex
    :param selAge: victim age
    :param selRelation: relationship
    :param selWeapon: weapon
    :return: predicted perpetrator age and sex for both the models
    '''
    sexModelDT = joblib.load('sexDT.pkl')
    sexModelAda = joblib.load('sexAda.pkl')
    ageModelDT = joblib.load('ageDT.pkl')
    ageModelAda = joblib.load('ageAda.pkl')
    sex1 = sexModelDT.predict([selSex, selAge, selRelation, selWeapon])
    sex2 = sexModelAda.predict([selSex, selAge, selRelation, selWeapon])
    age1 = ageModelDT.predict([selSex, selAge, selRelation, selWeapon])
    age2 = ageModelAda.predict([selSex, selAge, selRelation, selWeapon])
    return sex[sex1[0]], sex[sex2[0]], age[age1[0]], age[age2[0]]