import sys, os  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
#from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import ui  # Это наш конвертированный файл дизайна
from sensors import Sensor
from network import Network
from utils import degrees_to_cardinal, qt_message_handler
import urllib.request
import os
from datetime import datetime
import logging as log
from collections import deque
from gc import collect

class App(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.net = Network()
        self.sensor = Sensor()
        self.graph_data = deque()
        # Timer Periods
        self.switch_tab_period = 6000
        self.sensor_check_period = 1000
        self.graph_add_period = 1000 * 60
        self.graph_data_limit = 60
        self.new_weather_period = 1000 * 3200
        self.temperature, self.pressure, self.humidity = 0,0,0
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        work_dir = os.path.dirname(os.path.realpath(__file__))
        qssFile=work_dir + "/qss/darkStyle.qss"
        with open(qssFile,"r") as fh:
            self.setStyleSheet(fh.read())
        # Sensor Timer
        self.sensor_timer = QtCore.QTimer()
        self.sensor_timer.setInterval(1000)
        self.sensor_timer.timeout.connect(self.sensor_timer_process)
        self.sensor_timer.start()
        # Sensor Timer
        self.graph_timer = QtCore.QTimer()
        self.graph_timer.setInterval(self.graph_add_period)
        self.graph_timer.timeout.connect(self.update_graph)
        self.graph_timer.start()
        # Weather Timer
        self.weather_timer = QtCore.QTimer()
        self.weather_timer.setInterval(self.new_weather_period)
        self.weather_timer.timeout.connect(self.weather_timer_process)
        self.weather_timer.start()
        # Switch tabWidget
        self.switch_tab_timer = QtCore.QTimer()
        self.switch_tab_timer.setInterval(self.switch_tab_period)
        self.switch_tab_timer.timeout.connect(self.switch_tab)
        self.switch_tab_timer.start()
        # plotWidget
        background = QtGui.QBrush()
        background.setColor(QtGui.QColor(0x31363b))
        self.plot.setBackground(background)
        self.plot.getPlotItem().hideAxis('bottom')
        self.plot.getPlotItem().hideAxis('left')
        self.plot.getPlotItem().enableAutoRange(axis=None, enable=True, x=None, y=None)
        self.curve = self.plot.plot(pen=pg.mkPen('r', width=1, style=QtCore.Qt.SolidLine))
        # start
        self.weather_timer_process()
        log.info('User Interface Initialized')

    def update_graph(self):
        if len(self.graph_data) > self.graph_data_limit:
            self.graph_data.popleft() #remove oldest
        self.graph_data.append(self.pressure)
        self.curve.setData(self.graph_data)
        self.updown()
        self.statusbar.showMessage("Графік оновлено",5000)

    def updown(self):
        if self.curve.getData()[1][0] < self.pressure:
            self.sensor_updn_label.setText(chr(0x1eba))
        else:
            self.sensor_updn_label.setText(chr(0x1eb8))
    def switch_tab(self):
        if self.tabWidget.currentIndex() == 0:
            self.tabWidget.setCurrentIndex(1)
        else:
            self.tabWidget.setCurrentIndex(0)
    def set_weather_image(self, img):
        # image
        url = ' http://openweathermap.org/img/wn/' + img + '@2x.png'
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        self.image_label.setPixmap(QtGui.QPixmap(image))
    def set_forecast_image(self, img):
        # image
        url = ' http://openweathermap.org/img/wn/' + img + '@2x.png'
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        self.forecast_image_label.setPixmap(QtGui.QPixmap(image))
    def sensor_timer_process(self):
        time=QtCore.QDateTime.currentDateTime()
        timeDisplay=time.toString('hh:mm:ss')
        self.sensor_time_label.setText(timeDisplay)
        self.temperature, self.pressure, self.humidity = self.sensor.get_values()
        self.sensor_temp_label.setText(chr(0x1ebc) + str(round(self.temperature)) + chr(176))
        self.sensor_humi_label.setText(chr(0x1ec2) + ' ' + str(round(self.humidity)))
        self.sensor_press_label.setText(chr(0x1ebe) + str(round(self.pressure * 0.75)))
    def weather_timer_process(self):
        __raw = self.net.get_weather_data()
        current_weather = __raw['current']
        tomorrow_weather = __raw['daily'][1]
        self.weather_temperature_label.setText(str(round(current_weather['temp'])) + chr(176))
        self.weather_feels_label.setText(str(round(current_weather['feels_like'])) + chr(176))
        self.weather_humidity_label.setText(str(round(current_weather['humidity'])) + chr(0x1ec2))
        self.weather_pressure_label.setText(chr(0x1ebe) + " " + str(round(current_weather['pressure'] * 0.75)))
        self.weather_description_label.setText(current_weather['weather'][0]['description'])
        self.weather_wind_label.setText(chr(0x1ec0) + str(round(current_weather['wind_speed'])) + 'м/с ' + degrees_to_cardinal(current_weather['wind_deg']))
        self.weather_uvi_label.setText('UV: ' + str(round(current_weather['uvi'])))
        ob_time = datetime.fromtimestamp(current_weather['dt'])
        self.weather_time_label.setText(ob_time.strftime('%H:%M'))
        self.set_weather_image(current_weather['weather'][0]['icon'])
        # Forecast
        temp = chr(0x1e16) + str(round(tomorrow_weather['temp']['night'])) + chr(176) + " " + chr(0x1ec6) + " " + str(round(tomorrow_weather['temp']['day'])) + chr(176)
        self.forecast_temperature_label.setText(temp)
        #self.forecast_feels_label.setText(str(round(tomorrow_weather['feels_like']['day'])) + chr(176))
        self.forecast_humidity_label.setText(str(round(tomorrow_weather['humidity'])) + chr(0x1ec2))
        self.forecast_pressure_label.setText(chr(0x1ebe) + " " + str(round(tomorrow_weather['pressure'] * 0.75)))
        self.forecast_description_label.setText(tomorrow_weather['weather'][0]['description'])
        self.forecast_wind_label.setText(chr(0x1ec0) + str(round(tomorrow_weather['wind_speed'])) + 'м/с ' + degrees_to_cardinal(tomorrow_weather['wind_deg']))
        dt = datetime.fromtimestamp(tomorrow_weather['dt'])
        self.forecast_date_label.setText(dt.strftime('%d-%m-%Y'))
        self.set_forecast_image(tomorrow_weather['weather'][0]['icon'])
        self.statusbar.showMessage("Погода та прогноз оновлені",5000)
        collect()

def main():
    QtCore.qInstallMessageHandler(qt_message_handler)
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса App
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
