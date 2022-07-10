#Find the first maximum and second maximum number from integer array

import sys

def findFirstAndSecondMaximum(array):
    firstMaximum = -sys.maxsize-1
    secondMaximum =  -sys.maxsize-1
    for ele in array:
        if ele >firstMaximum:
            secondMaximum = firstMaximum
            firstMaximum = ele
    return firstMaximum,secondMaximum



array = [1,4,9,10,5,12,6,8]
firstMax,secondMax = findFirstAndSecondMaximum(array)
print(array)
print(firstMax,secondMax)
