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
	#FIXME: Unit conversion

    trigger = pyqtSignal(dict)
    def __init__(self, parent):
        QGroupBox.__init__(self, parent)
        self.ui = Ui_info_box()
        self.ui.setupUi(self)
        self.trigger.connect(self.set_data)
        self.connect(self.ui.weather_setter, SIGNAL("clicked()"), self.display_stuff)
        self.connect(self.ui.quitter, SIGNAL("clicked()"), qApp, SLOT("quit()"))
        self.connect(self.parent(), SIGNAL("close_pressed"), self.display_stuff)

    def display_stuff(self):
		self.trigger.emit({'current_conditions': {'temp_f': u'36',
		'temp_c': u'2', 'humidity': u'Humidity: 81%',
		'wind_condition': u'Wind: N at 6 mph', 'condition': u'Mostly Cloudy',
		'icon': u'/ig/images/weather/mostly_cloudy.gif'},
		'forecast_information': {'city': u'Karlsruhe, Baden-W\xfcrttemberg',
		'forecast_date': u'2011-01-20', 'latitude_e6': u'', 'longitude_e6': u'',
		'postal_code': u'karlsruhe', 'unit_system': u'US',
		'current_date_time': u'2011-01-20 19:00:00 +0000'},
		'forecasts': [{'high': u'37', 'condition': u'Chance of Snow',
		'low': u'26', 'day_of_week': u'Thu',
		'icon': u'/ig/images/weather/chance_of_snow.gif'}, {'high': u'32',
		'condition': u'Clear', 'low': u'24', 'day_of_week': u'Fri',
		'icon': u'/ig/images/weather/sunny.gif'}, {'high': u'32',
		'condition': u'Clear', 'low': u'21', 'day_of_week': u'Sat',
		'icon': u'/ig/images/weather/sunny.gif'}, {'high': u'32',
		'condition': u'Mostly Sunny', 'low': u'28', 'day_of_week': u'Sun',
		'icon': u'/ig/images/weather/mostly_sunny.gif'}]})

    def set_data(self, weather_data):
        self.ui.temp_high.setText(u"Current Temp.: " + 
        weather_data["current_conditions"]["temp_c"])
        self.ui.temp_low.setText(u"Morning High: " +
        weather_data["forecasts"][1]["high"])
        self.ui.condition.setText(u"Current Conditions: " +
        weather_data["current_conditions"]["condition"])
        self.ui.weather_icon.load("/usr/share/icons/ubuntu-mono-dark/status/24/sunny.svg")

class DataEngine(QObject):
	
	signal_set_data = pyqtSignal(dict)
	def __init__(self, location_code=u"groetzingen", parent=None):
		QObject.__init__(self, parent)
		self.location_code = location_code
		self.data = None
	
	def set_data(self):
		self.signal_set_data.emit(self.data)
	
	def update_data(self):
		new_data = pywapi.get_weather_from_google(self.location_code)
		if new_data != self.data:
			self.data = new_data
			self.set_data()
		else:
			new_data = None