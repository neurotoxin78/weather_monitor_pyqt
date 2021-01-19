import smbus2
import bme280

class Sensor(object):
    """docstring for Sensors."""

    def __init__(self):
        self.bus = smbus2.SMBus(0)
        self.address = 0x76
        compensation_params = bme280.load_calibration_params(self.bus, self.address)
    def get_values(self):
        data = bme280.sample(self.bus, self.address)
        return data.temperature, data.pressure, data.humidity
