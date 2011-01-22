# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupbox_test.ui'
#
# Created: Sat Jan 22 01:11:27 2011
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_info_box(object):
    def setupUi(self, info_box):
        info_box.setObjectName(_fromUtf8("info_box"))
        info_box.resize(317, 174)
        info_box.setFlat(False)
        info_box.setCheckable(False)
        info_box.setChecked(False)
        self.weather_icon = QSvgWidget(info_box)
        self.weather_icon.setGeometry(QtCore.QRect(30, 50, 50, 50))
        self.weather_icon.setObjectName(_fromUtf8("weather_icon"))
        self.temp_high = QtGui.QLabel(info_box)
        self.temp_high.setGeometry(QtCore.QRect(110, 50, 181, 17))
        self.temp_high.setObjectName(_fromUtf8("temp_high"))
        self.condition = QtGui.QLabel(info_box)
        self.condition.setGeometry(QtCore.QRect(20, 110, 251, 17))
        self.condition.setObjectName(_fromUtf8("condition"))
        self.temp_low = QtGui.QLabel(info_box)
        self.temp_low.setGeometry(QtCore.QRect(110, 80, 171, 17))
        self.temp_low.setObjectName(_fromUtf8("temp_low"))
        self.weather_setter = QtGui.QPushButton(info_box)
        self.weather_setter.setGeometry(QtCore.QRect(170, 140, 114, 27))
        self.weather_setter.setObjectName(_fromUtf8("weather_setter"))
        self.quitter = QtGui.QPushButton(info_box)
        self.quitter.setGeometry(QtCore.QRect(50, 140, 84, 22))
        self.quitter.setObjectName(_fromUtf8("quitter"))

        self.retranslateUi(info_box)
        QtCore.QMetaObject.connectSlotsByName(info_box)

    def retranslateUi(self, info_box):
        info_box.setWindowTitle(QtGui.QApplication.translate("info_box", "fail", None, QtGui.QApplication.UnicodeUTF8))
        info_box.setTitle(QtGui.QApplication.translate("info_box", "forecast_date", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_high.setText(QtGui.QApplication.translate("info_box", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.condition.setText(QtGui.QApplication.translate("info_box", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_low.setText(QtGui.QApplication.translate("info_box", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.weather_setter.setText(QtGui.QApplication.translate("info_box", "Set Weather", None, QtGui.QApplication.UnicodeUTF8))
        self.quitter.setText(QtGui.QApplication.translate("info_box", "Quit", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4.QtSvg import QSvgWidget
