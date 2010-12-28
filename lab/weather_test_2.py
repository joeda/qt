#!/usr/bin/python

#TODO: make a python unit conversion lib
#TODO: care about the standards

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *
from groupbox_test_ui import Ui_info_box
import collections
from dbus_interface import *
from clock_widget import ClockWidget
import time

weather = collections.namedtuple("Weather", "temperature condition icon")


class WeatherGetter(object):

    def __init__(self):
        pass

    def get_weather(self):
        pass


class ForecastWidget(QGroupBox):

    trigger = pyqtSignal(dict)
    def __init__(self, parent):
        QGroupBox.__init__(self, parent)
        self.ui = Ui_info_box()
        self.ui.setupUi(self)
        self.trigger.connect(self.set_weather)
        self.connect(self.ui.weather_setter, SIGNAL("clicked()"), self.display_stuff)
        self.connect(self.ui.quitter, SIGNAL("clicked()"), qApp, SLOT("quit()"))
        self.connect(self.parent(), SIGNAL("close_pressed"), self.display_stuff)

    def display_stuff(self):
        self.trigger.emit({"high":"20", "low":"10", "condition":"fail"})

    def set_weather(self, weather_data):
        self.ui.temp_high.setText(weather_data["high"])
        self.ui.temp_low.setText(weather_data["low"])
        self.ui.condition.setText(weather_data["condition"])
        self.ui.weather_icon.load("/usr/share/icons/ubuntu-mono-dark/status/24/sunny.svg")


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowFlags(Qt.Dialog)
        self.forecast1 = ForecastWidget(self)
        self.clock_widget = ClockWidget(self)
        hbox = QHBoxLayout()
        hbox.addWidget(self.clock_widget)
        hbox.addWidget(self.forecast1)
        vbox = QVBoxLayout()
        #vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.resize(400, 300)
        self.setFocus()

    def event(self, event):
#        if (event.type()==QEvent.KeyRelease) and ((event.key() == Qt.Key_Super_L)
#                or (event.key() == Qt.Key_T)) and event.isAutoRepeat() == False:
        if (event.type() == QEvent.KeyRelease and (event.key() == Qt.Key_Super_L
                or event.key() == Qt.Key_T) and event.isAutoRepeat() != True):
        #if event.type() == QEvent.KeyPress or event.type() == QEvent.KeyRelease:
            print "event type: " + str(event.type())
            print "event key: " + str(event.key())
            print "is autorepeat: " + str(event.isAutoRepeat())
            #self.emit(SIGNAL("close_pressed"))
            self.hide()
            return True

        return QWidget.event(self, event)

def main():
    dbus.mainloop.qt.DBusQtMainLoop(set_as_default = True)
    app = QApplication(sys.argv)
    main_win = MainWindow()
    db = DBusInterface(main_win)
    app.exec_()
    
if __name__ == "__main__":
    main()
