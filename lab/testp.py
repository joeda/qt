#from qt import *
from test_prog import Ui_MainWindow

class testp(test_prog):
    def __init__(self, parent=None, name=None, fl=0):
        test_prog.__init__(self,parent,name,fl)

if __name__ == "__main__":
    import sys
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = testp()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
