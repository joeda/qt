# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_applet.ui'
#
# Created: Thu Jul 22 18:11:54 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WeatherApplet(object):
    def setupUi(self, WeatherApplet):
        WeatherApplet.setObjectName("WeatherApplet")
        WeatherApplet.resize(640, 480)
        self.verticalLayoutWidget = QtGui.QWidget(WeatherApplet)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 260, 160, 88))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.graphicsView = QtGui.QGraphicsView(WeatherApplet)
        self.graphicsView.setGeometry(QtCore.QRect(280, 80, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.lcdNumber = QtGui.QLCDNumber(WeatherApplet)
        self.lcdNumber.setGeometry(QtCore.QRect(213, 302, 171, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.calendarWidget = QtGui.QCalendarWidget(WeatherApplet)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 40, 240, 165))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(WeatherApplet)
        QtCore.QMetaObject.connectSlotsByName(WeatherApplet)

    def retranslateUi(self, WeatherApplet):
        WeatherApplet.setWindowTitle(QtGui.QApplication.translate("WeatherApplet", "WeatherApplet", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("WeatherApplet", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("WeatherApplet", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("WeatherApplet", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

