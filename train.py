import csv
from sklearn import tree
from sklearn import ensemble

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

def computePercent(data1, data2):
    same = 0
    for i in range(len(data1)):
        if data1[i] == data2[i]:
            same += 1
    return same / len(data1) * 100

def predictResults(featureMatrix, model):
    result = model.predict(featureMatrix)
    return result

def trainModel(trainingFeatureMatrix, trainingLabels, model):
    model.fit(trainingFeatureMatrix, trainingLabels)
    return model

def buildPredMatrix(crime):
    predMatrix = list([])
    recordID = list([])
    for row in crime:
        if row[10] == 'No':
            if row[11] == 'Unknown' or row[12] == 0 or row[19] == 'Unknown' or row[20] == 'Unknown':
                pass
            else:
                row[11] = sex[row[11]]
                row[19] = relationship[row[19]]
                row[20] = weapon[row[20]]
                predMatrix.append([row[11], grouping(row[12]), row[19], row[20]])
                recordID.append(row[0])
    return predMatrix

def buildMatrixSex(crime):
    featureMatrix = list([])
    labels = list([])
    with open('perpetratorSexModelEvaluation.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

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
                    csvwriter.writerow([row[11], grouping(row[12]), row[19], row[20], sex[row[15]]])
    # return featureMatrix, labels

def buildMatrixAge(crime):
    featureMatrix = list([])
    labels = list([])
    with open('perpetratorAgeModelEvaluation.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
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
                    csvwriter.writerow([row[11], grouping(row[12]), row[19], row[20], grouping(row[16])])
    # return featureMatrix, labels

def init(filename):
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
    filename = 'cleaned.csv'
    crimeAge1 = init(filename)
    # buildMatrixSex(crimeAge1)
    buildMatrixAge(crimeAge1)

    # crimeSex1 = init(filename)
    # buildMatrixSex(crimeSex1)
    # crimeSex1 = init(filename)
    # crimeSex2 = init(filename)

    '''
    featureMatrixPerpAge1, labelsPerpAge1 = buildMatrixAge(crimeAge1)
    predMatrixPerpAge1 = buildPredMatrix(crimeAge1)
    modelAge1 = trainModel(featureMatrixPerpAge1, labelsPerpAge1, tree.DecisionTreeClassifier())
    resultAge1 = predictResults(predMatrixPerpAge1, modelAge1)

    featureMatrixPerpAge2, labelsPerpAge2 = buildMatrixAge(crimeAge2)
    predMatrixPerpAge2 = buildPredMatrix(crimeAge2)
    modelAge2 = trainModel(featureMatrixPerpAge2, labelsPerpAge2, ensemble.AdaBoostClassifier())
    resultAge2 = predictResults(predMatrixPerpAge2, modelAge2)

    print('Similartiy in Perpetrator Age prediction for Decision Tree and AdaBoost: ')
    print('%.2f'%computePercent(resultAge1,resultAge2))

    featureMatrixPerpSex1, labelsPerpSex1 = buildMatrixSex(crimeSex1)
    predMatrixPerpSex1 = buildPredMatrix(crimeSex1)
    modelSex1 = trainModel(featureMatrixPerpSex1, labelsPerpSex1, tree.DecisionTreeClassifier())
    resultSex1 = predictResults(predMatrixPerpSex1, modelSex1)

    featureMatrixPerpSex2, labelsPerpSex2 = buildMatrixSex(crimeSex2)
    predMatrixPerpSex2 = buildPredMatrix(crimeSex2)
    modelSex2 = trainModel(featureMatrixPerpSex2, labelsPerpSex2, ensemble.AdaBoostClassifier())
    resultSex2 = predictResults(predMatrixPerpSex2, modelSex2)

    print('Similartiy in Perpetrator Sex prediction for Decision Tree and AdaBoost: ')
    print('%.2f'%computePercent(resultSex1, resultSex2))
    '''

if __name__ == '__main__':
    main()