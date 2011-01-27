iimport dbus
import dbus.service
from PyQt4.QtCore import *
import dbus.mainloop.qt



class SignalEmitter(QObject):

    trigger = pyqtSignal()
    def __init__(self, reciever_object):
        QObject.__init__(self, parent=None)
        self.trigger.connect(reciever_object.thread.main_window.show)

    def emit_signal(self):
        self.trigger.emit()

class DBusInterface(dbus.service.Object):

    def __init__(self, reciever_object):
        session_bus = dbus.SessionBus()
        busName = dbus.service.BusName('org.joeda.weather_interface', session_bus)
        dbus.service.Object.__init__(self, busName, '/weather_interface')
        self.signal_emitter = SignalEmitter(reciever_object)

    @dbus.service.method("org.joeda.weather_interface", 
            in_signature="", out_signature="i")
    def HideWeather(self):
        self.signal_emitter.emit_signal()
        return 0

    @dbus.service.method("org.joeda.weather_interface",
            in_signature="", out_signature="s")
    def Hello(self):
        return "Hello, Human!"
