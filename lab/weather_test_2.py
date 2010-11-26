#!/usr/bin/python

# menubar.py 

#TODO: make a python unit conversion lib

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *
from groupbox_test_ui import Ui_info_box
import collections


weather = collections.namedtuple("Weather", "temperature condition icon")

class WeatherGetter(object):
	
	def __init__(self):
		pass
	
	def get_weather(self

class ForecastWidget(QGroupBox):

	trigger = pyqtSignal(dict)
	def __init__(self, parent):
		QGroupBox.__init__(self, parent)
		self.ui = Ui_info_box()
		self.ui.setupUi(self)
		self.trigger.connect(self.set_weather)
		self.connect(self.ui.weather_setter, SIGNAL("clicked()"), self.display_stuff)

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
sys.exit(app.exec_())
