#!/usr/bin/python

#TODO: make a python unit conversion lib
#TODO: care about the standards

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *
from groupbox_test_ui import Ui_info_box
import collections
import dbus.mainloop.qt
import dbus
import dbus.service


weather = collections.namedtuple("Weather", "temperature condition icon")


class WeatherGetter(object):

    def __init__(self):
        pass

    def get_weather(self):
        pass

class SignalEmitter(QObject):

    trigger = pyqtSignal()
    def __init__(self):
        QObject.__init__(self, parent=None)
        self.connect(self, SIGNAL("hide_weather"), qApp, SLOT("quit()"))

    def emit_signal(self):
        self.emit(SIGNAL("hide_weather"))

class DBusInterface(dbus.service.Object):

    def __init__(self):
        session_bus = dbus.SessionBus()
        busName = dbus.service.BusName('org.joeda.weather_interface', session_bus)
        dbus.service.Object.__init__(self, busName, '/weather_interface')
        self.signal_emitter = SignalEmitter()

    @dbus.service.method("org.joeda.weather_interface", 
            in_signature="", out_signature="i")
    def HideWeather(self):
        self.signal_emitter.emit_signal()
        return 0

    @dbus.service.method("org.joeda.weather_interface",
            in_signature="", out_signature="s")
    def Hello(self):
        return "Hello, Human!"
    
dbus.mainloop.qt.DBusQtMainLoop(set_as_default = True)

class ForecastWidget(QGroupBox):

    trigger = pyqtSignal(dict)
    def __init__(self, parent):
        QGroupBox.__init__(self, parent)
        self.ui = Ui_info_box()
        self.ui.setupUi(self)
        self.trigger.connect(self.set_weather)
        self.connect(self.ui.weather_setter, SIGNAL("clicked()"), self.display_stuff)
        self.connect(self.ui.quitter, SIGNAL("clicked()"), qApp, SLOT("quit()"))

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
        self.setWindowFlags(Qt.Dialog | Qt.X11BypassWindowManagerHint)
        forecast1 = ForecastWidget(self)
        forecast2 = ForecastWidget(self)
        hbox = QHBoxLayout()
        hbox.addWidget(forecast2)
        hbox.addWidget(forecast1)
        vbox = QVBoxLayout()
        #vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.resize(900, 600)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
db = DBusInterface()
app.exec_()
