import csv
import csv
import os.path

inputs = []
my_path = os.path.abspath(os.path.dirname(__file__))

with open(my_path + '/my-tests.csv', newline='') as csvfile:
    values = csv.reader(csvfile, delimiter=',')
    for row in values:
        array = []
        for i in row:
            array.append(float(i))
        inputs.append(array)
        # break

results = []

from numpy import array
from numpy.linalg import norm
for arr in inputs:
    results.append(norm(arr, 1))

print(results)