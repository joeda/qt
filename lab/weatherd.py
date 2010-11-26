
import dbus.mainloop.qt


INTERVAL = 5


#dbus.mainloop.qt.DBusQtMainLoop(set_as_default=True)
#session_dbus = dbus.SessionBus()

#class Emitter(dbus.service.Object):
	#def __init__(self, conn, object_path='/com/example/TestService/object'):
		#dbus.service.Object.__init__(self, conn, object_path)
	
	#@dbus.service.signal("com.example.TestService")
	
	#def new_weather_data(self, weather_data):
		#print weather_data
		#return

#emitter = Emitter(session_dbus)
#loop = gobject.MainLoop()
#loop.run()
#print "you can see me"

#class Example(dbus.service.Object):
    #def __init__(self, object_path):
        #dbus.service.Object.__init__(self, dbus.SessionBus(), path=None)

    #@dbus.service.signal(dbus_interface='com.example.Sample',
                         #signature='us')
    #def NumberOfBottlesChanged(self, number, contents):
        #print "%d bottles of %s on the wall" % (number, contents)

#e = Example(path="/bottle-counter")
#e.NumberOfBottlesChanged(100, "wall")
#print "lol"
# -*- coding: utf-8 -*-
# file: server.py
 
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
