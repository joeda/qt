import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pywapi
import time
sys.path.append("../")
import applet

class WeatherApplet(applet.Applet):
	def __init__(self):
		applet.Applet.__init__(self)

	def fetch_data(self, location):
		weather_data = pywapi.get_weather_from_google(location)
