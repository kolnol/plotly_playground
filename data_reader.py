import pandas as pd

from models.Measurements import Measurements
from models.MeasurementsType import MeasurementsType


def map_name_to_type(name) -> MeasurementsType:
    types_map = {
        'time': MeasurementsType.TIME,
        'tt': MeasurementsType.TEMPERATURE,
        'pt': MeasurementsType.PRESSURE
    }

    for k in types_map:
        if k in name.lower():
            return types_map[k]

    raise AttributeError(f'Cannot find suitable type for name {name}')


def read_from_csv(path) -> [Measurements]:
    measurements = []
    df = pd.read_csv(path)
    for column in df:
        measurements_type = map_name_to_type(column)
        name = column
        values = df[column]
        measurements.append(Measurements(measurements_type, values, name))

    return measurements


if __name__ == '__main__':
    test_measurements = read_from_csv('./data/test.csv')
    print(test_measurements)
