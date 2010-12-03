import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Applet(QWidget):

	def __init__(self, parent, conffile=None):

		QWidget.__init__(self, parent)

	def get_data(self):
		pass
