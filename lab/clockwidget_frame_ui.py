# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clockwidget_frame.ui'
#
# Created: Mon Dec 27 16:32:23 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(400, 300)
        Frame.setStyleSheet(_fromUtf8("QFrame {\n"
"    border: 2px solid blue;\n"
"    border-radius: 3px;\n"
"}"))
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Plain)
        self.label = QtGui.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Frame", "kahsdfhasdhfljkahsdjfklhajklsdfhjklahsfdjhasjdfhajlkshdfjalhsdflhasjkldfhakhsdfjklhasdjklfhajksdhfjkahsf", None, QtGui.QApplication.UnicodeUTF8))

