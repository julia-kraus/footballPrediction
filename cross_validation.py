from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import pandas as pd


def normalize_data(Xtrain, Xtest):
    sc = StandardScaler()
    X_train_std = sc.fit_transform(Xtrain)
    X_test_std = sc.transform(Xtest)

    return X_train_std, X_test_std


def read_data():
    X_train = pd.read_csv('Xtrain.csv', header=None).values
    X_test = pd.read_csv('Xtest.csv', header=None).values
    y_train = pd.read_csv('ytrain.csv', header=None).values.ravel()
    y_test = pd.read_csv('ytest.csv', header=None).values.ravel()
    return X_train, X_test, y_train, y_test




c_params = [0.0001, 0.001, 0.01, 0.1, 1.0, 10]
gamma_params = [0.0001, 0.001, 0.01, 0.1, 1.0, 10]
kernel_params = ['linear', 'rbf']

X_train, X_test, y_train, y_test = read_data()
parameters = [{'kernel': kernel_params, 'C': c_params, 'gamma':gamma_params}]

clf = SVC()
cv = GridSearchCV(clf, parameters)
cv.fit(X_train, y_train)
print(cv.best_estimator_)
print(cv.best_score_)


