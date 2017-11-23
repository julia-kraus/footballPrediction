from sklearn.preprocessing import StandardScaler
from sklearn import svm
import pandas as pd
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import itertools

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
    # Compute confusion matrix
    cnf_matrix = confusion_matrix(y_test, y_pred)
    np.set_printoptions(precision=2)

    # Plot non-normalized confusion matrix
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=['away', 'draw', 'home'],
                          title='Confusion matrix, without normalization')

    # Plot normalized confusion matrix
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=['away', 'draw', 'home'], normalize=True,
                          title='Normalized confusion matrix')


    plt.show()


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


doSVM()