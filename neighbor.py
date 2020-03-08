from knn_modules import distance
import operator


def get_neighbors(training_set, test_set, k, metric="euclidean"):
    distances = []
    length = len(test_set) - 1
    for x in range(len(training_set)):
        if metric == "euclidean":
            dist = distance.euclidean(test_set, training_set[x], length)
        else:
            dist = distance.manhattan(test_set, training_set[x], length)
        distances.append((training_set[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def get_response(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
