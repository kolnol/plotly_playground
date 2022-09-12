from data_reader import read_from_csv
import os

from visualisation import DataVisualiser


def main():
    path = os.path.join('data', 'test.csv')
    measurements = read_from_csv(path)

    visualiser = DataVisualiser()
    visualiser.build_graph(measurements)
    visualiser.show()


if __name__ == '__main__':
    main()
