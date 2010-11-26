#!/usr/bin/python

# ZetCode PyQt4 tutorial
#
# This example shows
# how to use QSplitter widget
# 
# author: Jan Bodnar
# website: zetcode.com
# last edited: February 2010


from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.initUI()


    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)

        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.Box)
 
        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.Box)

        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.Box)

        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(250, 200, 350, 250)
        self.setWindowTitle('QSplitter')

    

app = QtGui.QApplication([])
exm = Example()
exm.show()
app.exec_()

