# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_data.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(320, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(320, 240))
        MainWindow.setBaseSize(QtCore.QSize(320, 240))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background:rgb(91,90,90);")
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setBaseSize(QtCore.QSize(320, 240))
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:1, y1:0.529, x2:1, y2:0, stop:0.641791 rgba(80, 80, 80, 255), stop:1 rgba(39, 40, 44, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.main_tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tab_widget.setGeometry(QtCore.QRect(0, 0, 320, 241))
        self.main_tab_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_tab_widget.setAutoFillBackground(False)
        self.main_tab_widget.setStyleSheet("QWidget{background:transparent;\n"
"color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: rgb(157, 157, 157);\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    border-left: 0px transparent black;\n"
"    background-color: transparent;\n"
"    padding: 3px;\n"
"    min-width: 18px;\n"
"    min-height: 80px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab::selected {\n"
"    color: #eff0f1;\n"
"    background-color: rgb(120, 120, 120);\n"
"    border: 0px solid #76797C;\n"
"    border-left: 3px solid rgb(152, 152, 152);\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab::!selected:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.392672, y1:0.443, x2:0.0646766, y2:0.45, stop:0.606965 rgba(255, 55, 0, 0), stop:1 rgba(255, 111, 0, 240));\n"
"}\n"
"")
        self.main_tab_widget.setTabPosition(QtWidgets.QTabWidget.West)
        self.main_tab_widget.setElideMode(QtCore.Qt.ElideNone)
        self.main_tab_widget.setDocumentMode(True)
        self.main_tab_widget.setTabBarAutoHide(True)
        self.main_tab_widget.setObjectName("main_tab_widget")
        self.sensor_tab = QtWidgets.QWidget()
        self.sensor_tab.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:1, y1:0.529, x2:1, y2:0, stop:0.641791 rgba(80, 80, 80, 255), stop:1 rgba(39, 40, 44, 255));")
        self.sensor_tab.setObjectName("sensor_tab")
        self.sensor_tab_widget = QtWidgets.QTabWidget(self.sensor_tab)
        self.sensor_tab_widget.setGeometry(QtCore.QRect(0, 50, 291, 171))
        self.sensor_tab_widget.setStyleSheet("QWidget{background:transparent;\n"
"color: rgb(229, 229, 229);\n"
"}\n"
"/* TOP TABS */\n"
"QTabWidget {\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 0px solid #76797C;\n"
"    padding: 2px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"   left: 15px; \n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QTabBar:focus {\n"
"    border: 0px transparent black;\n"
"}\n"
"QTabBar::tab:top {\n"
"    color: rgb(154, 154, 154);\n"
"    border: 1px solid rgba(125, 125, 125, 100);\n"
"    border-right: 0px rgb(127, 127, 127);\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"    min-width: 80px;\n"
"    min-height: 18px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    color: #eff0f1;\n"
"    background-color:rgb(110, 110, 110);\n"
"    border: 1px solid rgba(105, 105, 105, 100);\n"
"    border-bottom: 1px solid rgb(255, 119, 0);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.393, y1:0.669636, x2:0.393, y2:0.915, stop:0.606965 rgba(255, 55, 0, 0), stop:1 rgba(255, 111, 0, 240));\n"
"}\n"
"")
        self.sensor_tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.sensor_tab_widget.setDocumentMode(True)
        self.sensor_tab_widget.setObjectName("sensor_tab_widget")
        self.tab_temperature = QtWidgets.QWidget()
        self.tab_temperature.setObjectName("tab_temperature")
        self.temp_plot = PlotWidget(self.tab_temperature)
        self.temp_plot.setGeometry(QtCore.QRect(4, 10, 275, 130))
        self.temp_plot.setStyleSheet("/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: transparent;\n"
"    color: #CDEBB7;\n"
"}")
        self.temp_plot.setObjectName("temp_plot")
        self.sensor_tab_widget.addTab(self.tab_temperature, "")
        self.tab_humidity = QtWidgets.QWidget()
        self.tab_humidity.setObjectName("tab_humidity")
        self.humi_plot = PlotWidget(self.tab_humidity)
        self.humi_plot.setGeometry(QtCore.QRect(4, 10, 275, 130))
        self.humi_plot.setStyleSheet("/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FB9902;\n"
"}")
        self.humi_plot.setObjectName("humi_plot")
        self.sensor_tab_widget.addTab(self.tab_humidity, "")
        self.tab_pressure = QtWidgets.QWidget()
        self.tab_pressure.setStyleSheet("")
        self.tab_pressure.setObjectName("tab_pressure")
        self.plot = PlotWidget(self.tab_pressure)
        self.plot.setGeometry(QtCore.QRect(4, 10, 275, 131))
        self.plot.setStyleSheet("background-color: transparent;\n"
"color: #FB9902;\n"
"")
        self.plot.setObjectName("plot")
        self.sensor_tab_widget.addTab(self.tab_pressure, "")
        self.sensor_temp_label = QtWidgets.QLabel(self.sensor_tab)
        self.sensor_temp_label.setGeometry(QtCore.QRect(4, 3, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_temp_label.setFont(font)
        self.sensor_temp_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #CDEBB7;\n"
"    font: 16pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_temp_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_temp_label.setObjectName("sensor_temp_label")
        self.sensor_press_label = QtWidgets.QLabel(self.sensor_tab)
        self.sensor_press_label.setGeometry(QtCore.QRect(185, 3, 71, 30))
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
"    color: #FE5010;\n"
"    font: 16pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_press_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_press_label.setObjectName("sensor_press_label")
        self.sensor_humi_label = QtWidgets.QLabel(self.sensor_tab)
        self.sensor_humi_label.setGeometry(QtCore.QRect(76, 3, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_humi_label.setFont(font)
        self.sensor_humi_label.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #5da6e2;\n"
"    font:16pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_humi_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_humi_label.setObjectName("sensor_humi_label")
        self.sensor_updn_label = QtWidgets.QLabel(self.sensor_tab)
        self.sensor_updn_label.setGeometry(QtCore.QRect(260, 3, 21, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_updn_label.setFont(font)
        self.sensor_updn_label.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FE5010;\n"
"    font: 20pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_updn_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_updn_label.setWordWrap(True)
        self.sensor_updn_label.setIndent(1)
        self.sensor_updn_label.setObjectName("sensor_updn_label")
        self.sensor_time_label = QtWidgets.QLabel(self.sensor_tab)
        self.sensor_time_label.setGeometry(QtCore.QRect(200, 215, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_time_label.setFont(font)
        self.sensor_time_label.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #E1ECF9;\n"
"    font: 11pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_time_label.setObjectName("sensor_time_label")
        self.sensor_press_max_label = QtWidgets.QLabel(self.sensor_tab)
        self.sensor_press_max_label.setGeometry(QtCore.QRect(210, 30, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Bold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_press_max_label.setFont(font)
        self.sensor_press_max_label.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FE5010;\n"
"    font: 8pt \"Source Sans Pro Bold\";\n"
"}")
        self.sensor_press_max_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_press_max_label.setObjectName("sensor_press_max_label")
        self.sensor_updn_humi_label = QtWidgets.QLabel(self.sensor_tab)
        self.sensor_updn_humi_label.setGeometry(QtCore.QRect(162, 3, 21, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_updn_humi_label.setFont(font)
        self.sensor_updn_humi_label.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #5da6e2;\n"
"    font: 20pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_updn_humi_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_updn_humi_label.setWordWrap(True)
        self.sensor_updn_humi_label.setIndent(1)
        self.sensor_updn_humi_label.setObjectName("sensor_updn_humi_label")
        self.sensor_updn_temp_label = QtWidgets.QLabel(self.sensor_tab)
        self.sensor_updn_temp_label.setGeometry(QtCore.QRect(66, 3, 21, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sensor_updn_temp_label.setFont(font)
        self.sensor_updn_temp_label.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #CDEBB7;\n"
"    font: 20pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.sensor_updn_temp_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sensor_updn_temp_label.setWordWrap(True)
        self.sensor_updn_temp_label.setIndent(1)
        self.sensor_updn_temp_label.setObjectName("sensor_updn_temp_label")
        self.statusbar = QtWidgets.QLabel(self.sensor_tab)
        self.statusbar.setGeometry(QtCore.QRect(30, 220, 171, 20))
        self.statusbar.setStyleSheet("/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FE5010;\n"
"    font: 11pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.statusbar.setText("")
        self.statusbar.setObjectName("statusbar")
        self.check_autoplay = QtWidgets.QCheckBox(self.sensor_tab)
        self.check_autoplay.setGeometry(QtCore.QRect(0, 220, 16, 20))
        self.check_autoplay.setStyleSheet("background-color: transparent;")
        self.check_autoplay.setObjectName("check_autoplay")
        self.main_tab_widget.addTab(self.sensor_tab, "")
        self.weaher_and_forecast_tab = QtWidgets.QWidget()
        self.weaher_and_forecast_tab.setObjectName("weaher_and_forecast_tab")
        self.tabWidget = QtWidgets.QTabWidget(self.weaher_and_forecast_tab)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 295, 220))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QWidget{background:transparent;\n"
"color: rgb(229, 229, 229);\n"
"}\n"
"/* TOP TABS */\n"
"QTabWidget {\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 0px solid #76797C;\n"
"    padding: 2px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"   left: 60px; \n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QTabBar:focus {\n"
"    border: 0px transparent black;\n"
"}\n"
"QTabBar::tab:top {\n"
"    color: rgb(154, 154, 154);\n"
"    border: 1px solid rgba(125, 125, 125, 100);\n"
"    border-right: 0px rgb(127, 127, 127);\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"    min-width: 80px;\n"
"    min-height: 18px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    color: #eff0f1;\n"
"    background-color: rgb(85, 85, 85);\n"
"    border: 1px solid rgba(105, 105, 105, 100);\n"
"    border-bottom: 1px solid rgb(255, 119, 0);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.393, y1:0.669636, x2:0.393, y2:0.915, stop:0.606965 rgba(255, 55, 0, 0), stop:1 rgba(255, 111, 0, 240));\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(1, 1))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.weather_tab = QtWidgets.QWidget()
        self.weather_tab.setObjectName("weather_tab")
        self.weather_description_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_description_label.setGeometry(QtCore.QRect(10, 165, 271, 21))
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
"    color: #ffa73c;\n"
"    font: 14pt \"Source Pro\";\n"
"}")
        self.weather_description_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.weather_description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_description_label.setObjectName("weather_description_label")
        self.weather_feels_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_feels_label.setGeometry(QtCore.QRect(200, 60, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.weather_feels_label.setFont(font)
        self.weather_feels_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #94D466;\n"
"    font: 20pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_feels_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weather_feels_label.setObjectName("weather_feels_label")
        self.weather_humidity_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_humidity_label.setGeometry(QtCore.QRect(180, 20, 71, 31))
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
"    color: #5da6e2;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_humidity_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.weather_humidity_label.setObjectName("weather_humidity_label")
        self.weather_temperature_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_temperature_label.setGeometry(QtCore.QRect(70, 50, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.weather_temperature_label.setFont(font)
        self.weather_temperature_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #CDEBB7;\n"
"    font: 50pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_temperature_label.setObjectName("weather_temperature_label")
        self.weather_wind_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_wind_label.setGeometry(QtCore.QRect(60, 130, 171, 21))
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
"    color: #ffa73c;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_wind_label.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_wind_label.setObjectName("weather_wind_label")
        self.weather_uvi_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_uvi_label.setGeometry(QtCore.QRect(210, 100, 71, 21))
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
        self.image_label.setGeometry(QtCore.QRect(10, 10, 80, 61))
        self.image_label.setLineWidth(0)
        self.image_label.setScaledContents(False)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.weather_pressure_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_pressure_label.setGeometry(QtCore.QRect(100, 20, 71, 31))
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
"    color: #FE5010;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.weather_pressure_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.weather_pressure_label.setObjectName("weather_pressure_label")
        self.weather_time_label = QtWidgets.QLabel(self.weather_tab)
        self.weather_time_label.setGeometry(QtCore.QRect(90, 0, 91, 21))
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
        self.weather_time_label.setAlignment(QtCore.Qt.AlignCenter)
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
        self.forecast_temperature_label.setGeometry(QtCore.QRect(20, 60, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.forecast_temperature_label.setFont(font)
        self.forecast_temperature_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #CDEBB7;\n"
"    font: 36pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.forecast_temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.forecast_temperature_label.setObjectName("forecast_temperature_label")
        self.forecast_humidity_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_humidity_label.setGeometry(QtCore.QRect(90, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.forecast_humidity_label.setFont(font)
        self.forecast_humidity_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #5da6e2;\n"
"    font: 18pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.forecast_humidity_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.forecast_humidity_label.setObjectName("forecast_humidity_label")
        self.forecast_pressure_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_pressure_label.setGeometry(QtCore.QRect(150, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.forecast_pressure_label.setFont(font)
        self.forecast_pressure_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #FE5010;\n"
"    font: 18pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.forecast_pressure_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.forecast_pressure_label.setObjectName("forecast_pressure_label")
        self.forecast_image_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_image_label.setGeometry(QtCore.QRect(5, 5, 80, 61))
        self.forecast_image_label.setScaledContents(False)
        self.forecast_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.forecast_image_label.setObjectName("forecast_image_label")
        self.forecast_description_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_description_label.setGeometry(QtCore.QRect(5, 150, 275, 31))
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
"    color: #ffa73c;\n"
"    font: 14pt \"Source Pro\";\n"
"}")
        self.forecast_description_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.forecast_description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.forecast_description_label.setObjectName("forecast_description_label")
        self.forecast_wind_label = QtWidgets.QLabel(self.forecast_tab)
        self.forecast_wind_label.setGeometry(QtCore.QRect(60, 120, 171, 21))
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
"    color: #ffa73c;\n"
"    font: 14pt \"Source Sans Pro SemiBold\";\n"
"}")
        self.forecast_wind_label.setAlignment(QtCore.Qt.AlignCenter)
        self.forecast_wind_label.setObjectName("forecast_wind_label")
        self.tabWidget.addTab(self.forecast_tab, "")
        self.main_tab_widget.addTab(self.weaher_and_forecast_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_tab_widget.setCurrentIndex(1)
        self.sensor_tab_widget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Погода та прогноз"))
        self.sensor_tab_widget.setTabText(self.sensor_tab_widget.indexOf(self.tab_temperature), _translate("MainWindow", "Температура"))
        self.sensor_tab_widget.setTabText(self.sensor_tab_widget.indexOf(self.tab_humidity), _translate("MainWindow", "Вологість"))
        self.sensor_tab_widget.setTabText(self.sensor_tab_widget.indexOf(self.tab_pressure), _translate("MainWindow", "Тиск"))
        self.sensor_temp_label.setText(_translate("MainWindow", "+20"))
        self.sensor_press_label.setText(_translate("MainWindow", "752"))
        self.sensor_humi_label.setText(_translate("MainWindow", "100%"))
        self.sensor_updn_label.setText(_translate("MainWindow", "0"))
        self.sensor_time_label.setText(_translate("MainWindow", "00:00"))
        self.sensor_press_max_label.setText(_translate("MainWindow", "max: 752"))
        self.sensor_updn_humi_label.setText(_translate("MainWindow", "0"))
        self.sensor_updn_temp_label.setText(_translate("MainWindow", "0"))
        self.check_autoplay.setText(_translate("MainWindow", "CheckBox"))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.sensor_tab), _translate("MainWindow", "Сенсор"))
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
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.weaher_and_forecast_tab), _translate("MainWindow", "Метеоданні"))

from pyqtgraph import PlotWidget
import darkstyle_rc
