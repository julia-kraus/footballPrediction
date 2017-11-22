from sklearn.preprocessing import StandardScaler
from sklearn import svm
import numpy as np
import create_training_test_data as cd
import pandas as pd


def normalize_data(Xtrain, Xtest):
    sc = StandardScaler()
    X_train_std = sc.fit_transform(Xtrain)
    X_test_std = sc.transform(Xtest)

    return X_train_std, X_test_std


def doSVM():
    # X_train = pd.read_csv('training_test_data_shuffled/Xtrain.csv', header=None).values
    # X_test = pd.read_csv('training_test_data_shuffled/Xtest.csv', header=None).values
    # y_train = pd.read_csv('training_test_data_shuffled/ytrain.csv', header=None).values
    # y_test = pd.read_csv('training_test_data_shuffled/ytest.csv', header=None).values
    #
    # X_train = X_train.flatten()
    # X_test = X_test.flatten()
    # y_train = y_train.flatten()
    # y_test = y_test.flatten()
    dataCreator = cd.TrainingTestDataGenerator()
    X_train, X_test, y_train, y_test = dataCreator.concatenate_training_test_data()


    detailResults = []
    X_train, X_test = normalize_data(X_train, X_test)

    predicthome = [0, 0, 0]
    predictdraw = [0, 0, 0]
    predictaway = [0, 0, 0]

    clf = svm.SVC(kernel='linear')
    clf.fit(X_train, y_train)
    print('the score is')
    print(clf.score)

    # right = 0
    # for temp in enumerate(X_test):
    #     detailResult = [X_test[temp[0]][2], X_test[temp[0]][3], X_test[temp[0]][6]]
    #     if (y_test[temp[0]] == 1):
    #         if (clf.predict(temp[1])[0] == 1):
    #             detailResult.append('H')
    #             right += 1
    #             predicthome[0] += 1
    #         elif (clf.predict(temp[1])[0] == 0):
    #             detailResult.append('D')
    #             predicthome[1] += 1
    #         else:
    #             detailResult.append('A')
    #             predicthome[2] += 1
    #     elif (y_test[temp[0]] == 0):
    #         if (clf.predict(temp[1])[0] == 1):
    #             detailResult.append('H')
    #             predictdraw[0] += 1
    #         elif (clf.predict(temp[1])[0] == 0):
    #             detailResult.append('D')
    #             right += 1
    #             predictdraw[1] += 1
    #         else:
    #             detailResult.append('A')
    #             predictdraw[2] += 1
    #     else:
    #         if (clf.predict(temp[1])[0] == 1):
    #             detailResult.append('H')
    #             predictaway[0] += 1
    #         elif (clf.predict(temp[1])[0] == 0):
    #             detailResult.append('D')
    #             predictaway[1] += 1
    #         else:
    #             detailResult.append('A')
    #             right += 1
    #             predictaway[2] += 1
    #     detailResults.append(detailResult)
    #
    # print(float(right) / len(y_test))
    # print(detailResults)
    # print(predicthome, predictdraw, predictaway)


def doSVMOnline(self):
    x, y = self.get_features_one_season()
    print(len(self.train_features))
    # scale_features = preprocessing.scale(np.array(self.trainFeatures,dtype = float))
    detailResults = []
    # scale_features = preprocessing.scale(np.array(x,dtype = float))
    # print scale_features
    tx = [x[1:] for x in self.test_features]
    ty = [x[0] for x in self.test_features]
    # print self.trainFeatures
    # print x
    # print y

    predicthome = [0, 0, 0]
    predictdraw = [0, 0, 0]
    predictaway = [0, 0, 0]

    clf = svm.SVC(kernel='rbf')
    clf.decision_function_shape = 'ovr'

    right = 0

    for temp in enumerate(tx):
        flag = 0
        clf.fit(x, y)

        detailResult = [self.test_set[temp[0]][2], self.test_set[temp[0]][3], self.test_set[temp[0]][6]]
        if (ty[temp[0]] == 1):
            if (clf.predict(temp[1])[0] == 1):
                detailResult.append('H')
                right += 1
                flag = 1
                predicthome[0] += 1
            elif (clf.predict(temp[1])[0] == 0):
                detailResult.append('D')
                predicthome[1] += 1
            else:
                detailResult.append('A')
                predicthome[2] += 1
        elif (ty[temp[0]] == 0):
            if (clf.predict(temp[1])[0] == 1):
                detailResult.append('H')
                predictdraw[0] += 1
            elif (clf.predict(temp[1])[0] == 0):
                detailResult.append('D')
                right += 1
                flag = 1
                predictdraw[1] += 1
            else:
                detailResult.append('A')
                predictdraw[2] += 1
        else:
            if (clf.predict(temp[1])[0] == 1):
                detailResult.append('H')
                predictaway[0] += 1
            elif (clf.predict(temp[1])[0] == 0):
                detailResult.append('D')
                predictaway[1] += 1
            else:
                detailResult.append('A')
                right += 1
                flag = 1
                predictaway[2] += 1
        detailResults.append(detailResult)

        if (flag == 0):
            ##update training set
            newTrainEx = self.combine_label_and_features(self.test_set[temp[0]][2], self.test_set[temp[0]][3],
                                                         self.test_set[temp[0]][1], self.test_set[temp[0]][6], 'E2015')
            print(newTrainEx)
            x.append(newTrainEx[1:])
            y.append(newTrainEx[0])

    print(float(right) / len(tx))
    print(detailResults)
    print(predicthome, predictdraw, predictaway)


doSVM()
