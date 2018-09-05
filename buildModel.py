'''
Authors: Eshaan Shah, Anindo Saha, Rohit Mudaliar
This py file is used to build the models
'''

import csv
from sklearn import tree
from sklearn import ensemble
from sklearn.externals import joblib

weapon = {
    'Blunt Object': 0,
    'Strangulation': 1,
    'Rifle': 2,
    'Knife': 3,
    'Firearm': 4,
    'Shotgun': 5,
    'Fall': 6,
    'Handgun': 7,
    'Drowning': 8,
    'Suffocation': 9,
    'Explosives': 10,
    'Fire': 11,
    'Drugs': 12,
    'Gun': 13,
    'Poison': 14
}

relationship = {
    'Acquaintance': 0,
    'Wife': 1,
    'Stranger': 2,
    'Girlfriend': 3,
    'Ex-Husband': 4,
    'Brother': 5,
    'Stepdaughter': 6,
    'Husband': 7,
    'Sister': 8,
    'Friend': 9,
    'Family': 10,
    'Neighbor': 11,
    'Father': 12,
    'In-Law': 13,
    'Son': 14,
    'Ex-Wife': 15,
    'Boyfriend': 16,
    'Mother': 17,
    'Common-Law Husband': 18,
    'Common-Law Wife': 19,
    'Stepfather': 20,
    'Stepson': 21,
    'Stepmother': 22,
    'Daughter': 23,
    'Boyfriend/Girlfriend': 24,
    'Employer': 25,
    'Employee': 26
}

sex = {
    'Male': 0,
    'Female': 1
}

def grouping(value):
    '''
    Converts age into categoric data
    :param value: age
    :return: category
    '''
    if value < 11:
        return 0
    elif 10 < value < 21:
        return 1
    elif 20 < value < 31:
        return 2
    elif 30 < value < 41:
        return 3
    elif 40 < value < 51:
        return 4
    elif 50 < value < 61:
        return 5
    elif 60 < value < 71:
        return 6
    elif 70 < value < 81:
        return 7
    elif 80 < value < 91:
        return 8
    return 9

def trainModel(trainingFeatureMatrix, trainingLabels, model):
    '''
    Trains the model
    :param trainingFeatureMatrix: feature matrix
    :param trainingLabels: labels
    :param model: model to be trained
    :return: trained model
    '''
    model.fit(trainingFeatureMatrix, trainingLabels)
    return model

def buildMatrixSex(crime):
    '''
    Builds feature matrix for sex models
    :param crime: list
    :return: feature matrix
    '''
    featureMatrix = list([])
    labels = list([])
    for row in crime:
        if row[10] == 'Yes':
            if row[11] == 'Unknown' or row[12] == 0 or row[15] == 'Unknown' or \
                            row[19] == 'Unknown' or row[20] == 'Unknown':
                pass
            else:
                row[11] = sex[row[11]]
                row[19] = relationship[row[19]]
                row[20] = weapon[row[20]]
                featureMatrix.append([row[11], grouping(row[12]), row[19], row[20]])
                labels.append(sex[row[15]])
    return featureMatrix, labels

def buildMatrixAge(crime):
    '''
    Builds feature matrxi for training age model
    :param crime: list
    :return: feature matrix
    '''
    featureMatrix = list([])
    labels = list([])
    for row in crime:
        if row[10] == 'Yes':
            if row[11] == 'Unknown' or row[12] == 0 or row[16] == 0 or \
                            row[19] == 'Unknown' or row[20] == 'Unknown':
                pass
            else:
                row[11] = sex[row[11]]
                row[19] = relationship[row[19]]
                row[20] = weapon[row[20]]
                featureMatrix.append([row[11], grouping(row[12]), row[19], row[20]])
                labels.append(grouping(row[16]))
    return featureMatrix, labels

def init(filename):
    '''
    Reads the input data set and stores the data in a py list
    :param filename: data set file
    :return: list
    '''
    crime = list([])
    flag = 0
    with open(filename) as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            if flag == 0:
                flag += 1
                continue
            row[12] = int(row[12])
            row[16] = int(row[16])
            row[0] = int(row[0])
            crime.append(row)
    return crime

def main():
    '''
    Main function
    takes the input data set
    calls other functions in appropriate order
    :return: None
    '''
    filename = 'cleaned.csv'
    crimeAge1 = init(filename)
    crimeAge2 = init(filename)
    crimeSex1 = init(filename)
    crimeSex2 = init(filename)

    featureMatrixPerpAge1, labelsPerpAge1 = buildMatrixAge(crimeAge1)
    ageModelDT = trainModel(featureMatrixPerpAge1, labelsPerpAge1, tree.DecisionTreeClassifier())
    joblib.dump(ageModelDT, 'ageDT.pkl')

    featureMatrixPerpAge2, labelsPerpAge2 = buildMatrixAge(crimeAge2)
    ageModelAda = trainModel(featureMatrixPerpAge2, labelsPerpAge2, ensemble.AdaBoostClassifier())
    joblib.dump(ageModelAda, 'ageAda.pkl')

    featureMatrixPerpSex1, labelsPerpSex1 = buildMatrixSex(crimeSex1)
    sexModelDT = trainModel(featureMatrixPerpSex1, labelsPerpSex1, tree.DecisionTreeClassifier())
    joblib.dump(sexModelDT, 'sexDT.pkl')

    featureMatrixPerpSex2, labelsPerpSex2 = buildMatrixSex(crimeSex2)
    sexModelAda = trainModel(featureMatrixPerpSex2, labelsPerpSex2, ensemble.AdaBoostClassifier())
    joblib.dump(sexModelAda, 'sexAda.pkl')

if __name__ == '__main__':
    main()