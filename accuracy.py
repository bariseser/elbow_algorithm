def get_accuracy(test_data, predictions):
    correct = 0
    for x in range(len(test_data)):
        if test_data[x][-1] in predictions[x]:
            correct = correct + 1

    return correct / float(len(test_data)) * 100
