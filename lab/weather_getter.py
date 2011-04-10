# -*- coding: utf-8 -*-
# file: client.py

import dbus

bus = dbus.SessionBus()
server = bus.get_object('org.documentroot.Calculator', '/Calculator')
print '5 and 10 are:',
print server.add(5, 10, dbus_interface = 'org.documentroot.Calculator')
print 'the factorial of 6 is:',
print server.factorial(6, dbus_interface = 'org.documentroot.Calculator')
