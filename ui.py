# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(320, 240)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        MainWindow.setMaximumSize(QtCore.QSize(320, 240))
        MainWindow.setBaseSize(QtCore.QSize(320, 240))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(320, 213))
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.sensor_humi_label = QtWidgets.QLabel(self.centralwidget)
        self.sensor_humi_label.setGeometry(QtCore.QRect(8, 33, 81, 26))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_humi_label.setFont(font)
        self.sensor_humi_label.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #678FFE;\n"
"    font: 20pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_humi_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sensor_humi_label.setObjectName("sensor_humi_label")
        self.sensor_temp_label = QtWidgets.QLabel(self.centralwidget)
        self.sensor_temp_label.setGeometry(QtCore.QRect(5, 5, 71, 26))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_temp_label.setFont(font)
        self.sensor_temp_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #CDEBB7;\n"
"    font: 20pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_temp_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sensor_temp_label.setObjectName("sensor_temp_label")
        self.plot = PlotWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(139, 0, 181, 90))
        self.plot.setStyleSheet("/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FB9902;\n"
"}")
        self.plot.setObjectName("plot")
        self.sensor_press_label = QtWidgets.QLabel(self.centralwidget)
        self.sensor_press_label.setGeometry(QtCore.QRect(64, 5, 71, 26))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_press_label.setFont(font)
        self.sensor_press_label.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FD8F3B;\n"
"    font: 16pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_press_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_press_label.setObjectName("sensor_press_label")
        self.sensor_updn_label = QtWidgets.QLabel(self.centralwidget)
        self.sensor_updn_label.setGeometry(QtCore.QRect(80, 30, 56, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_updn_label.setFont(font)
        self.sensor_updn_label.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FD8F3B;\n"
"    font: 24pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_updn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_updn_label.setWordWrap(True)
        self.sensor_updn_label.setIndent(1)
        self.sensor_updn_label.setObjectName("sensor_updn_label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 90, 320, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.weather_tab = QtWidgets.QWidget()
        self.weather_tab.setObjectName("weather_tab")
        self.weather_description_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_description_label.setGeometry(QtCore.QRect(55, 58, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Source Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.weather_description_label.setFont(font)
        self.weather_description_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FDCE6F;\n"
"    font: 14pt \"Source Pro\";\n"
"}")
        self.weather_description_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.weather_description_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weather_description_label.setObjectName("weather_description_label")
        self.weather_feels_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_feels_label.setGeometry(QtCore.QRect(60, 5, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.weather_feels_label.setFont(font)
        self.weather_feels_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #94D466;\n"
"    font: 16pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_feels_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weather_feels_label.setObjectName("weather_feels_label")
        self.weather_humidity_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_humidity_label.setGeometry(QtCore.QRect(5, 33, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.weather_humidity_label.setFont(font)
        self.weather_humidity_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #678FFE;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_humidity_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.weather_humidity_label.setObjectName("weather_humidity_label")
        self.weather_temperature_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_temperature_label.setGeometry(QtCore.QRect(130, 0, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.weather_temperature_label.setFont(font)
        self.weather_temperature_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #CDEBB7;\n"
"    font: 40pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_temperature_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.weather_temperature_label.setObjectName("weather_temperature_label")
        self.weather_wind_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_wind_label.setGeometry(QtCore.QRect(1, 58, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.weather_wind_label.setFont(font)
        self.weather_wind_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FDCE6F;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_wind_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.weather_wind_label.setObjectName("weather_wind_label")
        self.weather_uvi_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_uvi_label.setGeometry(QtCore.QRect(5, 18, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.weather_uvi_label.setFont(font)
        self.weather_uvi_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #9191F0;\n"
"    font: 12pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_uvi_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.weather_uvi_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.weather_uvi_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.weather_uvi_label.setObjectName("weather_uvi_label")
        self.image_label = QtWidgets.QLabel(self.weather_tab)
        self.image_label.setGeometry(QtCore.QRect(230, 0, 80, 61))
        self.image_label.setScaledContents(False)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.weather_pressure_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_pressure_label.setGeometry(QtCore.QRect(60, 33, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.weather_pressure_label.setFont(font)
        self.weather_pressure_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FD8F3B;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_pressure_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weather_pressure_label.setObjectName("weather_pressure_label")
        self.weather_time_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_time_label.setGeometry(QtCore.QRect(5, 0, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.weather_time_label.setFont(font)
        self.weather_time_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FBFDE2;\n"
"    font: 12pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_time_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.weather_time_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.weather_time_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.weather_time_label.setObjectName("weather_time_label")
        self.tabWidget.addTab(self.weather_tab, "")
        self.forecast_tab = QtWidgets.QWidget()
        self.forecast_tab.setObjectName("forecast_tab")
        self.forecast_date_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_date_label.setGeometry(QtCore.QRect(90, 5, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.forecast_date_label.setFont(font)
        self.forecast_date_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FBFDE2;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.forecast_date_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.forecast_date_label.setObjectName("forecast_date_label")
        self.forecast_temperature_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_temperature_label.setGeometry(QtCore.QRect(110, 31, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.forecast_temperature_label.setFont(font)
        self.forecast_temperature_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #CDEBB7;\n"
"    font: 20pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.forecast_temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.forecast_temperature_label.setObjectName("forecast_temperature_label")
        self.forecast_humidity_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_humidity_label.setGeometry(QtCore.QRect(215, 0, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.forecast_humidity_label.setFont(font)
        self.forecast_humidity_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #678FFE;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.forecast_humidity_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.forecast_humidity_label.setObjectName("forecast_humidity_label")
        self.forecast_pressure_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_pressure_label.setGeometry(QtCore.QRect(255, 0, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.forecast_pressure_label.setFont(font)
        self.forecast_pressure_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FD8F3B;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.forecast_pressure_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.forecast_pressure_label.setObjectName("forecast_pressure_label")
        self.forecast_image_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_image_label.setGeometry(QtCore.QRect(0, 0, 80, 61))
        self.forecast_image_label.setScaledContents(False)
        self.forecast_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.forecast_image_label.setObjectName("forecast_image_label")
        self.forecast_description_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_description_label.setGeometry(QtCore.QRect(5, 55, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Source Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.forecast_description_label.setFont(font)
        self.forecast_description_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FDCE6F;\n"
"    font: 14pt \"Source Pro\";\n"
"}")
        self.forecast_description_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.forecast_description_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.forecast_description_label.setObjectName("forecast_description_label")
        self.forecast_wind_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_wind_label.setGeometry(QtCore.QRect(135, 55, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.forecast_wind_label.setFont(font)
        self.forecast_wind_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FDCE6F;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.forecast_wind_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.forecast_wind_label.setObjectName("forecast_wind_label")
        self.tabWidget.addTab(self.forecast_tab, "")
        self.sensor_time_label = QtWidgets.QLabel(self.centralwidget)
        self.sensor_time_label.setGeometry(QtCore.QRect(0, 64, 141, 26))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_time_label.setFont(font)
        self.sensor_time_label.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FBFDE2;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_time_label.setObjectName("sensor_time_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statusbar.setFont(font)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Погода та прогноз"))
        self.sensor_humi_label.setText(_translate("MainWindow", "100%"))
        self.sensor_temp_label.setText(_translate("MainWindow", "20"))
        self.sensor_press_label.setText(_translate("MainWindow", "752"))
        self.sensor_updn_label.setText(_translate("MainWindow", "0"))
        self.weather_description_label.setText(_translate("MainWindow", "description"))
        self.weather_feels_label.setText(_translate("MainWindow", "00"))
        self.weather_humidity_label.setText(_translate("MainWindow", "000"))
        self.weather_temperature_label.setText(_translate("MainWindow", "00"))
        self.weather_wind_label.setText(_translate("MainWindow", "wind"))
        self.weather_uvi_label.setText(_translate("MainWindow", "uvi:"))
        self.image_label.setText(_translate("MainWindow", "image"))
        self.weather_pressure_label.setText(_translate("MainWindow", "000"))
        self.weather_time_label.setText(_translate("MainWindow", "00:00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weather_tab), _translate("MainWindow", "Погода"))
        self.forecast_date_label.setText(_translate("MainWindow", "00/00/0000"))
        self.forecast_temperature_label.setText(_translate("MainWindow", "00"))
        self.forecast_humidity_label.setText(_translate("MainWindow", "000"))
        self.forecast_pressure_label.setText(_translate("MainWindow", "000"))
        self.forecast_image_label.setText(_translate("MainWindow", "image"))
        self.forecast_description_label.setText(_translate("MainWindow", "description"))
        self.forecast_wind_label.setText(_translate("MainWindow", "wind"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.forecast_tab), _translate("MainWindow", "Прогноз"))
        self.sensor_time_label.setText(_translate("MainWindow", "00:00"))

from pyqtgraph import PlotWidget
