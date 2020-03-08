import csv


def load(filename):
    training_data = []
    test_data = []
    with open(filename, 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if x in range(0, 30) or x in range(51, 81) or x in range(101, 131):
                training_data.append(dataset[x])
            else:
                test_data.append(dataset[x])
    return [training_data, test_data]
