
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pywapi
import time
import applets


class Main_window(QWidget):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        self.thread = Worker()
        self.setGeometry(200, 200, 400, 400)
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setFrameRect(QRect(10,10, 200, 200))
        quitter = QPushButton("Quit", self.frame)
        quitter.setGeometry(10, 10, 60, 35)
        self.connect(quitter, SIGNAL("clicked()"), qApp, SLOT("quit()"))
        self.nowLoading = QLabel("Loading weather data...", self.frame)
        self.nowLoading.move(10, 60)
        self.connect(self.thread, SIGNAL("output(QString)"), self.handle_weather_data)
        self.thread.start()

    def handle_weather_data(self, data):
        print "data: ", data
        self.nowLoading.setText(data)

class Applet(QWidget):

    def __init__(self, parent=main_window):

        QWidget.__init__(self, parent)

class Worker(QThread):
    def __init__(self, parent=None):

        QThread.__init__(self, parent)
        print "__init__ worked"

    def run(self):
        time.sleep(2)
        weather_data = pywapi.get_weather_from_google("de-76187")
        res = "temp: " + weather_data["current_conditions"]["temp_c"]
        res = QString(res)
        print "run worked"
        print res
        self.emit(SIGNAL("output(QString)"), res)
print "test"
wa = applets.WeatherApplet()
ap = QApplication(sys.argv)
main_window = Main_window()
main_window.show()
sys.exit(ap.exec_())
