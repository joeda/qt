import dbus.mainloop.qt
from PyQt4.QtCore import *
import math
import dbus
import dbus.service

class Calculator(dbus.service.Object):
    def __init__(self):
        busName = dbus.service.BusName('org.documentroot.Calculator', bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, busName, '/Calculator')

    @dbus.service.method('org.documentroot.Calculator', in_signature = 'dd', out_signature = 'd')
    def add(self, a, b): return a+b

    @dbus.service.method('org.documentroot.Calculator', in_signature = 'i', out_signature = 'i')
    def factorial(self, n): return 1 if n <= 1 else n*self.factorial(n-1)

    @dbus.service.method('org.documentroot.Calculator', in_signature = 'd', out_signature = 'd')
    def sqrt(self, n): return math.sqrt(n)

    @dbus.service.method('org.documentroot.Calculator', in_signature = 'd', out_signature = 'i')
    def round(self, n): return round(n)

dbus.mainloop.qt.DBusQtMainLoop(set_as_default = True)
app = QCoreApplication([])
calc = Calculator()
app.exec_()
