from models import MeasurementsType


class Measurements:
    def __init__(self, measurements_type: MeasurementsType, values, name):
        self.measurements_type = measurements_type
        self.values = values
        self.name = name

