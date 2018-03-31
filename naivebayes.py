import sys
import numpy as np
import csv
from os.path import dirname, exists, expanduser, isdir, join, splitext
import os 
# Gaussian Naive Bayes

from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


def load_data(cwd, data_file_name):
    with open(join(cwd, 'upload', data_file_name)) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        target_names = np.array(temp[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=np.int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[:-1], dtype=np.float64)
            target[i] = np.asarray(ir[-1], dtype=np.int)

    return data, target, target_names


# command line arguments
filename = sys.argv[1]

#current working directory
cwd = os.getcwd()

# load the iris datasets
data, target, target_names = load_data(cwd, filename)
# print(data,target,target_names)

# fit a Naive Bayes model to the data
model = GaussianNB()
model.fit(data, target)

# make predictions
predicted = model.predict(data)

# summarize the fit of the model
# print(metrics.classification_report(target, predicted))

# print(metrics.confusion_matrix(target, predicted))
score = accuracy_score(target, predicted)
print(score)
