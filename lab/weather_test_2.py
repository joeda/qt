#!/usr/bin/python

#TODO: make a python unit conversion lib
#TODO: care about the standards

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *
import collections
from dbus_interface import *
from clock_widget import ClockWidget
from weather_widget import WeatherWidget

weather = collections.namedtuple("Weather", "temperature condition icon")


MAIN_WIN_HEIGHT = 500
MAIN_WIN_WIDTH = 600


class WeatherGetter(object):

    def __init__(self):
        pass

    def get_weather(self):
        pass


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowFlags(Qt.Dialog)
        self.weather_widget = WeatherWidget(self)
        self.clock_widget = ClockWidget(self)
        hbox = QHBoxLayout()
        hbox.addWidget(self.clock_widget)
        hbox.addWidget(self.weather_widget)
        vbox = QVBoxLayout()
        #vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.resize(MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT)
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
