FEET_TO_METER_RATIO = 0.3048


class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # create convert_height here
    def convert_height(self):
        return self.height / FEET_TO_METER_RATIO
