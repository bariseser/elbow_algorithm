from knn_modules import knn
from knn_modules import neighbor
from knn_modules import accuracy as ac


def main():
    predictions = []
    data = knn.load('iris.csv')
    training_set = data[0]
    test_set = data[1]
    errorCount = 0
    correctCount = 0

    k = 7
    for x in range(len(test_set)):
        neighbors = neighbor.get_neighbors(training_set, test_set[x], k, "euclidean")
        result = neighbor.get_response(neighbors)
        predictions.append(result)
        if repr(result) == repr(test_set[x][-1]):
            correctCount += 1
        else:
            errorCount += 1

    accuracy = ac.get_accuracy(test_set, predictions)

    print('Train set:', len(training_set), "iris")
    print('Test set:', len(test_set), "iris")
    print('K Value = ', k)
    print('Accuracy: ', round(accuracy, 2))
    print('Error Count:', errorCount, "/", correctCount)


main()
