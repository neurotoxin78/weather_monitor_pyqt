import sys, os  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
import paho.mqtt.client as mqtt
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
from scipy.optimize import curve_fit
import numpy as np
import darkstyle
collect()

class App(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.net = Network()
        self.sensor = Sensor()
        self.graph_data = deque()
        self.humi_graph_data = deque()
        self.temp_graph_data = deque()
        # Timer Periods
        self.switch_weather_tab_period = 6000
        self.switch_sensor_tab_period = 4000
        self.switch_main_tab_period = 12000
        self.sensor_check_period = 1000
        self.graph_add_period = 1000  * 60
        self.graph_data_limit = 60
        self.humi_graph_add_period = 1000 * 60
        self.humi_graph_data_limit = 60
        self.temp_graph_add_period = 1000 * 60
        self.temp_graph_data_limit = 60
        self.new_weather_period = 1000 * 3200
        self.temperature, self.pressure, self.humidity = 0,0,0
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        work_dir = os.path.dirname(os.path.realpath(__file__))
        qssFile=work_dir + "/darkstyle.qss"
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
        # humi graph_data
        self.humi_graph_timer = QtCore.QTimer()
        self.humi_graph_timer.setInterval(self.humi_graph_add_period)
        self.humi_graph_timer.timeout.connect(self.update_humi_graph)
        self.humi_graph_timer.start()
        # temp graph_data
        self.temp_graph_timer = QtCore.QTimer()
        self.temp_graph_timer.setInterval(self.temp_graph_add_period)
        self.temp_graph_timer.timeout.connect(self.update_temp_graph)
        self.temp_graph_timer.start()
        # Weather Timer
        self.weather_timer = QtCore.QTimer()
        self.weather_timer.setInterval(self.new_weather_period)
        self.weather_timer.timeout.connect(self.weather_timer_process)
        self.weather_timer.start()
        #switch_sensor_tab
        self.switch_main_tab_timer = QtCore.QTimer()
        self.switch_main_tab_timer.setInterval(self.switch_main_tab_period)
        self.switch_main_tab_timer.timeout.connect(self.switch_main_tab)
        self.switch_main_tab_timer.start()
        # Switch weather
        self.switch_weather_tab_timer = QtCore.QTimer()
        self.switch_weather_tab_timer.setInterval(self.switch_weather_tab_period)
        self.switch_weather_tab_timer.timeout.connect(self.switch_weather_tab)
        self.switch_weather_tab_timer.start()
        #switch_sensor_tab
        self.switch_sensor_tab_timer = QtCore.QTimer()
        self.switch_sensor_tab_timer.setInterval(self.switch_sensor_tab_period)
        self.switch_sensor_tab_timer.timeout.connect(self.switch_sensor_tab)
        self.switch_sensor_tab_timer.start()
        # plotWidget
        background = QtGui.QBrush()
        background.setColor(QtGui.QColor(0x31363b))
        l = pg.LegendItem((10,10), offset=(60,75))  # args are (size, offset)
        l.setParentItem(self.plot.graphicsItem())   # Note we do NOT call plt.addItem in this case
        self.plot.setBackground(background)
        self.plot.addLegend()
        self.plot.plotItem.showGrid(x=True, y=True, alpha=0.3)
        self.plot.getPlotItem().addLegend()
        self.plot.getPlotItem().enableAutoRange(axis=None, enable=True, x=None, y=None)
        self.curve = self.plot.plot(pen=pg.mkPen('r', width=1, name="атмосферний тиск", symbol='o',symbolPen='r', symbolBrush=0.5, style=QtCore.Qt.SolidLine))
        l.addItem(self.curve, 'атмосферний тиск mmHg')
        #humi plotWidget
        # plotWidget
        self.humi_plot.setBackground(background)
        lh = pg.LegendItem((10,10), offset=(95,75))  # args are (size, offset)
        lh.setParentItem(self.humi_plot.graphicsItem())   # Note we do NOT call plt.addItem in this case
        self.humi_plot.plotItem.showGrid(x=True, y=True, alpha=0.3)
        self.humi_plot.getPlotItem().enableAutoRange(axis=None, enable=True, x=None, y=None)
        self.humi_curve = self.humi_plot.plot(pen=pg.mkPen('b', width=1, style=QtCore.Qt.SolidLine))
        lh.addItem(self.humi_curve, 'вологість %')
        #temp plotWidget
        # plotWidget
        self.temp_plot.setBackground(background)
        lh = pg.LegendItem((10,10), offset=(95,75))  # args are (size, offset)
        lh.setParentItem(self.temp_plot.graphicsItem())   # Note we do NOT call plt.addItem in this case
        self.temp_plot.plotItem.showGrid(x=True, y=True, alpha=0.3)
        self.temp_plot.getPlotItem().enableAutoRange(axis=None, enable=True, x=None, y=None)
        self.temp_curve = self.temp_plot.plot(pen=pg.mkPen('g', width=1, style=QtCore.Qt.SolidLine))
        lh.addItem(self.temp_curve, 'температура ' + chr(176) + 'C')
        # QRC
        icon = QtGui.QIcon(":/checkbox_unchecked_disabled")
        self.statusbar.setPixmap(QtGui.QPixmap(":/icon_branch_open"))
        # mqtt
        self.mqtt_client =mqtt.Client('bme280')
        self.mqtt_client.connect('localhost')
        # Styling

        # start
        self.tabWidget.setCurrentIndex(0)
        self.weather_timer_process()
        #self.update_graph()
        #self.update_humi_graph()
        log.info('User Interface Initialized')

    def update_temp_graph(self):
        if len(self.temp_graph_data) > self.temp_graph_data_limit:
            self.temp_graph_data.popleft() #remove oldest
        self.temp_graph_data.append(self.temperature)
        self.temp_curve.setData(self.temp_graph_data)
        self.temp_updown()

    def update_humi_graph(self):
        if len(self.humi_graph_data) > self.humi_graph_data_limit:
            self.humi_graph_data.popleft() #remove oldest
        self.humi_graph_data.append(self.humidity)
        self.humi_curve.setData(self.humi_graph_data)
        self.humi_updown()

    def update_graph(self):
        if len(self.graph_data) > self.graph_data_limit:
            self.graph_data.popleft() #remove oldest
        self.graph_data.append(self.pressure * 0.750062)
        self.curve.setData(self.graph_data)
        #flatten = np.array(self.graph_data).flatten(order='F')
        #print(flatten.max(), flatten.size)
        #self.statusbar.showMessage('max:' +str(round(flatten.max() * 0.75,2)) + ' min:' +str(round(flatten.min() * 0.75,2)) + ' e:' + str(flatten.size))
        #self.curve.setData(flatten)
        self.press_updown()
        #self.statusbar.showMessage("Графік оновлено",5000)

    def press_updown(self):
        maximum = round(self.curve.getData()[1][0], 2)
        last_item = round(self.curve.getData()[1][-1], 2)
        #print(maximum, last_item)
        self.sensor_press_max_label.setText('max:' + str(maximum))
        if maximum < last_item:
            self.sensor_updn_label.setText(chr(0x1eba)) # UP
        elif maximum == last_item:
            self.sensor_updn_label.setText(chr(0x2248)) # # approx equal
        else:
            self.sensor_updn_label.setText(chr(0x1eb8)) # down
    def humi_updown(self):
        maximum = round(self.humi_curve.getData()[1][0], 2)
        last_item = round(self.humi_curve.getData()[1][-1], 2)
        #print(maximum, last_item)
        if maximum < last_item:
            self.sensor_updn_humi_label.setText(chr(0x1eba)) # UP
        elif maximum == last_item:
            self.sensor_updn_humi_label.setText(chr(0x2248)) # approx equal
        else:
            self.sensor_updn_humi_label.setText(chr(0x1eb8)) # down
    def temp_updown(self):
        maximum = round(self.temp_curve.getData()[1][0], 2)
        last_item = round(self.temp_curve.getData()[1][-1], 2)
        #print(maximum, last_item)
        if maximum < last_item:
            self.sensor_updn_temp_label.setText(chr(0x1eba)) # UP
        elif maximum == last_item:
            self.sensor_updn_temp_label.setText(chr(0x2248)) # approx equal
        else:
            self.sensor_updn_temp_label.setText(chr(0x1eb8)) # down
    def switch_weather_tab(self):
        #print(self.tabWidget.count())
        if self.tabWidget.currentIndex() == self.tabWidget.count() - 1:
            self.tabWidget.setCurrentIndex(0)
        else:
            self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() + 1)
    def switch_sensor_tab(self):
        #print(self.tabWidget.count())
        if self.sensor_tab_widget.currentIndex() == self.sensor_tab_widget.count() - 1:
            self.sensor_tab_widget.setCurrentIndex(0)
        else:
            self.sensor_tab_widget.setCurrentIndex(self.sensor_tab_widget.currentIndex() + 1)
    def switch_main_tab(self):
        #print(self.tabWidget.count())
        if self.main_tab_widget.currentIndex() == self.main_tab_widget.count() - 1:
            self.main_tab_widget.setCurrentIndex(0)
        else:
            self.main_tab_widget.setCurrentIndex(self.main_tab_widget.currentIndex() + 1)
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
        self.sensor_temp_label.setText(chr(0x1ebc) + str(self.mk_temp(round(self.temperature))) + chr(176))
        self.sensor_humi_label.setText(chr(0x1ec2) + ' ' + str(round(self.humidity)))
        self.sensor_press_label.setText(chr(0x1ebe) + str(round(self.pressure * 0.75)))
        self.mqtt_client.publish("orangepi/sensors/bme280/temperature",self.temperature)
        self.mqtt_client.publish("orangepi/sensors/bme280/humidity",self.humidity)
        self.mqtt_client.publish("orangepi/sensors/bme280/pressure",self.pressure)

    def weather_timer_process(self):
        __raw = self.net.get_weather_data()
        current_weather = __raw['current']
        tomorrow_weather = __raw['daily'][1]
        temp = self.mk_temp(round(current_weather['temp']))
        self.weather_temperature_label.setText(str(temp) + chr(176))
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
        temp = chr(0x1e16) + str(self.mk_temp(round(tomorrow_weather['temp']['night']))) + chr(176) + " " + chr(0x1ec6) + " " + str(self.mk_temp(round(tomorrow_weather['temp']['day']))) + chr(176)
        self.forecast_temperature_label.setText(temp)
        #self.forecast_feels_label.setText(str(round(tomorrow_weather['feels_like']['day'])) + chr(176))
        self.forecast_humidity_label.setText(str(round(tomorrow_weather['humidity'])) + chr(0x1ec2))
        self.forecast_pressure_label.setText(chr(0x1ebe) + " " + str(round(tomorrow_weather['pressure'] * 0.75)))
        self.forecast_description_label.setText(tomorrow_weather['weather'][0]['description'])
        self.forecast_wind_label.setText(chr(0x1ec0) + str(round(tomorrow_weather['wind_speed'])) + 'м/с ' + degrees_to_cardinal(tomorrow_weather['wind_deg']))
        dt = datetime.fromtimestamp(tomorrow_weather['dt'])
        self.forecast_date_label.setText(dt.strftime('%d-%m-%Y'))
        self.set_forecast_image(tomorrow_weather['weather'][0]['icon'])
        collect()
    def mk_temp(self, temp):
        if temp > 0:
            return "+" + str(temp)
        elif temp == 0:
            return str(temp)
        else:
            return str(temp)

def main():
    QtCore.qInstallMessageHandler(qt_message_handler)
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса App
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
