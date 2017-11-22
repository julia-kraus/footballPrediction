from sklearn.preprocessing import StandardScaler
from sklearn import svm
import pandas as pd
from sklearn.metrics import confusion_matrix

# still to do: shuffle X_train, y_train

def normalize_data(Xtrain, Xtest):
    sc = StandardScaler()
    X_train_std = sc.fit_transform(Xtrain)
    X_test_std = sc.transform(Xtest)

    return X_train_std, X_test_std


def doSVM():
    X_train = pd.read_csv('Xtrain.csv', header=None).values
    X_test = pd.read_csv('Xtest.csv', header=None).values
    y_train = pd.read_csv('ytrain.csv', header=None).values.ravel()
    y_test = pd.read_csv('ytest.csv', header=None).values.ravel()
    #


    X_train, X_test = normalize_data(X_train, X_test)


    clf = svm.SVC(kernel='linear')
    clf.fit(X_train, y_train)
    print('the score is')
    print(clf.score(X_test, y_test))
    y_pred = clf.predict(X_test)
    print(confusion_matrix(y_test, y_pred))

    # create confusion matrix with scikit learn

        # extra Funktion machen
        # if (flag == 0):
        #     ##update training set
        #     newTrainEx = self.combine_label_and_features(self.test_set[temp[0]][2], self.test_set[temp[0]][3],
        #                                                  self.test_set[temp[0]][1], self.test_set[temp[0]][6], 'E2015')
        #     print(newTrainEx)
        #     x.append(newTrainEx[1:])
        #     y.append(newTrainEx[0])



doSVM()
