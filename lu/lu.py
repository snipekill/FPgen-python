import csv
import numpy as np
import os.path
import scipy
import scipy.linalg

inputs = []
outputs = []
my_path = os.path.abspath(os.path.dirname(__file__))

with open(my_path + '/my-tests.csv', newline='') as csvfile:
    values = csv.reader(csvfile, delimiter=',')
    for row in values:
        array = []
        for i in row:
            array.append(float(i))
        A = np.reshape(array[0:16], (4,4))
        inputs.append([A])
        P, L, U = scipy.linalg.lu(A)
        outputs.append([P, L, U])
        # break

print(np.sum(outputs[0]))
