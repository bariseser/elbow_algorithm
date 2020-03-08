import math


def euclidean(test, training, length):
    distance = 0
    for x in range(length):
        distance += pow((test[x] - training[x]), 2)
    return math.sqrt(distance)


def manhattan(test, training, length):
    distance = 0
    for x in range(length):
        distance += abs(test[x] - training[x])
    return distance
