
import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import config_parser

def main():
	app = QApplication(sys.argv)
	Dsotd = Main_window()
	Dsotd.show()
	sys.exit(app.exec_())

class Main_window(QWidget):
	def __init__(self, parent=None):

		QWidget.__init__(self, parent)
		self._setup_config()
		self._setup_main()
		self._setup_applets()

	def _setup_config(self):

		conffile_parser = config_parser.ConfigParser()
		self.config = conffile_parser.setup_config()

	def _setup_main(self):

		self.setGeometry(self.config["main"]["left"], self.config["main"]["top"], self.config["main"]["width"], self.config["main"]["height"])
		self.frame = QFrame(self)
		self.frame.setFrameShape(QFrame.StyledPanel)

	def _setup_applets(self):

		self._applets = self.config["main"]["applets"]

if __name__ == "__main__":
	main()
