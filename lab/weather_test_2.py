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
from weather_widget import DataEngine
import os

weather = collections.namedtuple("Weather", "temperature condition icon")


MAIN_WIN_HEIGHT = 500
MAIN_WIN_WIDTH = 600
LOCATION_CODE = "Karlsruhe"
CONFIG_DIR = os.getcwd()
CONFFILE_NAME_DATA = "config_data_thread.json"
ENGINES_NAME_IN_CONFIG = "engines"
ENGINES_DIR_NAME_IN_CONFIG = "engines_directory"



class ConfigParser(object):

    def __init__(self, config_dir=None):
        self.config_dir = config_dir

    def get_config(self, conffile_name):

        # The directories follow the freedesktop.org standards, except that
        # custom applets go to XDG_CONFIG_HOME/dsotd/applets
        if not self.config_dir:
            if os.environ.has_key("XDG_CONFIG_HOME"):
                self.config_dir = os.path.join(os.environ["XDG_CONFIG_HOME"], "dsotd")
            else:
                self.config_dir = os.path.join(os.environ["HOME"], ".config/dsotd")
        if not os.access(os.path.join(self.config_dir, conffile_name), os.R_OK):
            raise IOError("No configuration file found!")

        conffile = open(os.path.join(self.config_dir, CONFIG_FILE))
        self.config = json.load(conffile)
        return self.config


class WidgetsDirectoryParser(object):

    def __init__(self):
        pass

    def look_for_widgets(self, directory, list_of_necessary_files=None):
        widgets = []
        os.chdir(directory)
        entries = os.listdir(directory)
        for entry in entries:
            if os.path.isdir(entry):
                for the_file in list_of_necessary_files:
                    if os.access(os.path.join(entry, the_file), os.R_OK):
                        widgets.append(entry)
                return widgets


class DataThread(QObject):

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.config_parser = ConfigParser(config_dir=CONFIG_DIR)
        self.config = self.config_parser.get_config(CONFFILE_NAME_DATA)
        self._update_path()
        self.engines = self._setup_engines()
        self.thread = WindowThread()
        self.weather_data_engine = DataEngine(location_code=LOCATION_CODE)
        self.weather_data_engine.signal_set_data.connect(
        self.thread.main_window.weather_widget.forecast1.set_data)
        self.weather_data_engine.update_data()

    def _update_path(self):
        sys.path.append(self.config[ENGINES_DIR_NAME_IN_CONFIG])

    def _setup_engines(self):
        return_dict = {}
        engines = self.config[ENGINES_NAME_IN_CONFIG].keys()
        for engine in engines:
            pass



class WindowThread(QThread):

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.main_window = MainWindow()

    def run(self):
        pass

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
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
    main_win = DataThread()
    db = DBusInterface(main_win)
    app.exec_()

if __name__ == "__main__":
    main()
