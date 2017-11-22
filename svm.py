from sklearn import preprocessing
from sklearn import svm
import numpy as np
import create_training_test_data as cd

def doSVM(self):
    
    print(len(self.train_features))
    detailResults = []
    scale_features = preprocessing.scale(np.array(x, dtype=float))
    print(scale_features)

    predicthome = [0, 0, 0]
    predictdraw = [0, 0, 0]
    predictaway = [0, 0, 0]

    clf = svm.SVC(kernel='linear')
    clf.fit(X_train, y_train)

    right = 0
    for temp in enumerate(X_test):
        detailResult = [self.test_set[temp[0]][2], self.test_set[temp[0]][3], self.test_set[temp[0]][6]]
        if (y_test[temp[0]] == 1):
            if (clf.predict(temp[1])[0] == 1):
                detailResult.append('H')
                right += 1
                predicthome[0] += 1
            elif (clf.predict(temp[1])[0] == 0):
                detailResult.append('D')
                predicthome[1] += 1
            else:
                detailResult.append('A')
                predicthome[2] += 1
        elif (y_test[temp[0]] == 0):
            if (clf.predict(temp[1])[0] == 1):
                detailResult.append('H')
                predictdraw[0] += 1
            elif (clf.predict(temp[1])[0] == 0):
                detailResult.append('D')
                right += 1
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
                predictaway[2] += 1
        detailResults.append(detailResult)

    print(float(right) / len(y_test))
    print(detailResults)
    print(predicthome, predictdraw, predictaway)


def doSVMOnline(self):
    x, y = self.get_features_one_season()
    print(len(self.train_features))
    # scale_features = preprocessing.scale(np.array(self.trainFeatures,dtype = float))
    detailResults = []
    # scale_features = preprocessing.scale(np.array(x,dtype = float))
    # print scale_features
    print(x[-1])
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


gameP = GamePredictor()
gameP.doSVMOnline()
