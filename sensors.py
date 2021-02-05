
class Sensor(object):
    """docstring for Sensors."""

    def __init__(self):
        self.temperature_file = '/sys/bus/iio/devices/iio:device0/in_temp_input'
        self.humidity_file = '/sys/bus/iio/devices/iio:device0/in_humidityrelative_input'
        self.pressure_file = '/sys/bus/iio/devices/iio:device0/in_pressure_input'
    def __get_temperature(self):
        with open(self.temperature_file) as file:
            return file.read()
    def __get_humidity(self):
        with open(self.humidity_file) as file:
            return file.read()
    def __get_pressure(self):
        with open(self.pressure_file) as file:
            return file.read()
    def get_values(self):
        temperature = float(self.__get_temperature())  / 1000
        humidity = float(self.__get_humidity()) / 1000
        pressure = float(self.__get_pressure()) * 10
        return temperature, pressure, humidity
