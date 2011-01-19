from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pywapi
from groupbox_test_ui import Ui_info_box

class WeatherWidget(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self)
        self.forecast1 = ForecastWidget(self)
        self.forecast2 = ForecastWidget(self)
        vbox = QVBoxLayout()
        vbox.addWidget(self.forecast1)
        vbox.addWidget(self.forecast2)
        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        self.setLayout(hbox)


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

class DataEngine(QObject):
	
	signal_set_data = pyqtSignal(dict)
	def __init__(self, location_code):
		QObject.__init__(self, parent)
		self.location_code = location_code
		self.data = None
	
	def set_data(self):
		self.signal_set_data.emit(self.data)
	
	def update_data(self, location_code):
		new_data = pywapi.get_weather_from_google(location_code)
		if new_data != self.data:
			self.data = new_data
			self.set_data()
		else:
			new_data = None