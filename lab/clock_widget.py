from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time

class ClockWidget(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self)

        # It is important to subclass any QtGui base class and apply the
        # stylesheet to the subclass, otherwise the stylesheet will apply
        # to any instance of the QtGui base class!
        self.setStyleSheet("""ClockWidget {
                border: 2px solid blue;
                border-radius: 4px;
                }""")
        self.resize(300,400)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(10, 10, 200, 300))
        self.label.setText("ahsdfjhasdjkhflashdfhasdjfhajklshdasldhkfjashdfjklhaskldjf")

        
