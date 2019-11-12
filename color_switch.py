from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import device_handler
import Ui_SWW
    
if __name__ == '__main__':   
    app = QtWidgets.QApplication(sys.argv)
    SWW = QtWidgets.QWidget()
    ui = Ui_SWW.Ui_SWW()
    ui.setupUi(SWW)
    SWW.move(SWW.width() * -3, 0)
    SWW.show()
    device_handler.device_handler(0,0,0)
    Ui_SWW.move2RightBottomCorner(SWW)

    ex = Ui_SWW.Ui_SWW()
    sys.exit(app.exec_())