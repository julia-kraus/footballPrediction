from sklearn.preprocessing import StandardScaler
from sklearn import svm
import pandas as pd
from sklearn.metrics import confusion_matrix
import random

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


    X_train, X_test = normalize_data(X_train, X_test)

    clf = svm.SVC(kernel='rbf')
    clf.fit(X_train, y_train)
    print('the score is')
    print(clf.score(X_test, y_test))
    y_pred = clf.predict(X_test)
    print(confusion_matrix(y_test, y_pred))


doSVM()
