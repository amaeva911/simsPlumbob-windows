# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'styles.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import device_handler
import time



class Ui_SWW(object):
    def setupUi(self, SWW):
        SWW.setObjectName("SWW")
        SWW.resize(400, 295)
        SWW.setWindowIcon(QtGui.QIcon('img/2.jpg'))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SWW.sizePolicy().hasHeightForWidth())
        SWW.setSizePolicy(sizePolicy)
        SWW.setMinimumSize(QtCore.QSize(0, 0))
        SWW.setMaximumSize(QtCore.QSize(400, 320))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        SWW.setFont(font)
        SWW.setAutoFillBackground(False)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(SWW)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 381, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.status_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")
        self.verticalLayout_2.addWidget(self.status_label)
        self.status_combo = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.status_combo.setEnabled(True)
        self.status_combo.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.status_combo.setFont(font)
        self.status_combo.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.status_combo.setToolTip("")
        self.status_combo.setAccessibleName("")
        self.status_combo.setInputMethodHints(QtCore.Qt.ImhNone)
        self.status_combo.setEditable(False)
        self.status_combo.setObjectName("status_combo")
        self.status_combo.addItem("Не выбрано")
        self.status_combo.addItem("Свободна")
        self.status_combo.addItem("Занята")
        self.status_combo.addItem("Совещание")
        self.status_combo.addItem("Не подходить!")
        self.status_combo.addItem("Мозговой штурм")
        self.status_combo.addItem("Не работаю")
        self.verticalLayout_2.addWidget(self.status_combo)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(SWW)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 100, 381, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mode_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.mode_label.setFont(font)
        self.mode_label.setObjectName("mode_label")
        self.verticalLayout_3.addWidget(self.mode_label)
        self.mode_combo = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.mode_combo.setEnabled(True)
        self.mode_combo.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.mode_combo.setFont(font)
        self.mode_combo.setAcceptDrops(True)
        self.mode_combo.setToolTip("")
        self.mode_combo.setEditable(False)
        self.mode_combo.setObjectName("mode_combo")
        self.mode_combo.addItem("Не выбрано")
        self.mode_combo.addItem("Свободный RGB")
        # self.mode_combo.addItem("Randomizer")
        self.mode_combo.addItem("Police")
        self.mode_combo.addItem("45/15")
        self.mode_combo.addItem("120/15")
        self.verticalLayout_3.addWidget(self.mode_combo)
        self.R_spinBox = QtWidgets.QSpinBox(SWW)
        self.R_spinBox.setGeometry(QtCore.QRect(30, 200, 60, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.R_spinBox.sizePolicy().hasHeightForWidth())
        self.R_spinBox.setSizePolicy(sizePolicy)
        self.R_spinBox.setMinimumSize(QtCore.QSize(60, 40))
        self.R_spinBox.setMaximumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.R_spinBox.setFont(font)
        self.R_spinBox.setMaximum(250)
        self.R_spinBox.setObjectName("B_spinBox")
        self.R_label = QtWidgets.QLabel(SWW)
        self.R_label.setEnabled(True)
        self.R_label.setGeometry(QtCore.QRect(0, 200, 20, 40))
        self.R_label.setMinimumSize(QtCore.QSize(10, 0))
        self.R_label.setMaximumSize(QtCore.QSize(20, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.R_label.setFont(font)
        self.R_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.R_label.setObjectName("R_label")
        self.G_spinBox = QtWidgets.QSpinBox(SWW)
        self.G_spinBox.setGeometry(QtCore.QRect(130, 200, 60, 40))
        self.G_spinBox.setMinimumSize(QtCore.QSize(60, 40))
        self.G_spinBox.setMaximumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.G_spinBox.setFont(font)
        self.G_spinBox.setMaximum(250)
        self.G_spinBox.setObjectName("G_spinBox")
        self.G_label = QtWidgets.QLabel(SWW)
        self.G_label.setGeometry(QtCore.QRect(100, 200, 20, 40))
        self.G_label.setMinimumSize(QtCore.QSize(10, 0))
        self.G_label.setMaximumSize(QtCore.QSize(20, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.G_label.setFont(font)
        self.G_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.G_label.setObjectName("G_label")
        self.B_spinBox = QtWidgets.QSpinBox(SWW)
        self.B_spinBox.setGeometry(QtCore.QRect(230, 200, 60, 40))
        self.B_spinBox.setMinimumSize(QtCore.QSize(60, 40))
        self.B_spinBox.setMaximumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.B_spinBox.setFont(font)
        self.B_spinBox.setMaximum(250)
        # self.R_spinBox.setProperty("value", 1)
        self.B_spinBox.setDisplayIntegerBase(10)
        self.B_spinBox.setObjectName("R_spinBox")
        self.B_label = QtWidgets.QLabel(SWW)
        self.B_label.setEnabled(True)
        self.B_label.setGeometry(QtCore.QRect(210, 200, 10, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B_label.sizePolicy().hasHeightForWidth())
        self.B_label.setSizePolicy(sizePolicy)
        self.B_label.setMinimumSize(QtCore.QSize(10, 0))
        self.B_label.setMaximumSize(QtCore.QSize(10, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.B_label.setFont(font)
        self.B_label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.B_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.B_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.B_label.setObjectName("B_label")
        self.warning_label = QtWidgets.QLabel(SWW)
        self.warning_label.setGeometry(QtCore.QRect(30, 245, 380, 40))
        self.warning_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.warning_label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.warning_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.warning_label.setFont(font)
        self.warning_label.setText("")
        self.warning_label.setTextFormat(QtCore.Qt.AutoText)
        self.warning_label.setObjectName("warning_label")

        self.button = QtWidgets.QPushButton(SWW)
        self.button.setGeometry(QtCore.QRect(310, 200, 80, 40))
        self.button.setMaximumSize(QtCore.QSize(80, 40))
        self.button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(8)
        self.button.setFont(font)
        self.button.setObjectName("B_label")
        self.button.setText("Применить")





        Ui_SWW.onVisible(self, False)

        self.status_combo.activated[str].connect(self.onActivatedStatus)
        self.mode_combo.activated[str].connect(self.onActivatedMode)
        self.status_combo.currentTextChanged.connect(self.onCurrentStatusChanged)
        self.mode_combo.currentTextChanged.connect(self.onCurrentModeChanged)

        self.button.clicked.connect(self.buttonClicked)



        self.retranslateUi(SWW)
        # QtCore.QMetaObject.connectSlotsByName(SWW)


    def onCurrentStatusChanged(self, text):
        self.mode_combo.setCurrentIndex(0)
    def onCurrentModeChanged(self, text):
        self.status_combo.setCurrentIndex(0)
    
    def onActivatedStatus(self, text):

        if (text == "Не работаю" or text == "Не выбрано"):
            device_handler.device_handler(0,0,0)
            Ui_SWW.onVisible(self, False)
        if (text == "Свободна"):
            # self.mode_combo.setItem("Не выбрано")
            device_handler.device_handler(0,250,0)
            Ui_SWW.onVisible(self, False)
                # if isLamp.isLamp():
                #     device_handler.device_handler(0,250,0)
                # else:
                #     self.warning = "isLamp.isLamp() "
        if (text == "Занята"):
            device_handler.device_handler(250,250,0)
            Ui_SWW.onVisible(self, False)
        if (text == "Совещание"):
            device_handler.device_handler(250,0,250)
            Ui_SWW.onVisible(self, False)
        if (text == "Не подходить!"):
            device_handler.device_handler(250,0,0)
            Ui_SWW.onVisible(self, False)
        if (text == "Мозговой штурм"):
            device_handler.device_handler(0,250,250)
            Ui_SWW.onVisible(self, False)
            
    def onActivatedMode(self, text):
        if (text == "Свободный RGB"):
            device_handler.device_handler(0,0,0)
            Ui_SWW.onVisible(self, True)
        if (text == "Randomizer"):
            # self.mode_combo.setItem("Не выбрано")
            device_handler.device_handler(0,250,0)
                # if isLamp.isLamp():
                #     device_handler.device_handler(0,250,0)
                # else:
                #     self.warning = "isLamp.isLamp() "
            Ui_SWW.onVisible(self, False)
        if (text == "Police"):
            Ui_SWW.police(self)
        if (text == "45/15"):
            Ui_SWW.fif(self)
        if (text == "120/15"):
            Ui_SWW.sanpin(self)

    def onVisible(self, isCheck):
        if isCheck == False:
            self.button.hide()
            self.R_label.hide()
            self.G_label.hide()
            self.B_label.hide()
            self.R_spinBox.hide()
            self.G_spinBox.hide()
            self.B_spinBox.hide()

        if isCheck == True:
            self.button.show()
            self.R_label.show()
            self.G_label.show()
            self.B_label.show()
            self.R_spinBox.show()
            self.G_spinBox.show()
            self.B_spinBox.show()

    def buttonClicked(self):
        r = self.R_spinBox.value() 
        g = self.G_spinBox.value() 
        b = self.B_spinBox.value() 
        device_handler.device_handler(r,g,b)
        # self.warning_label.setText(f'{r} - 123')

    def police(self):
        while (self.mode_combo.currentText() == "Police"):
            device_handler.device_handler(250,0,0)
            time.sleep(2)
            device_handler.device_handler(0,0,250)
            time.sleep(2)

    def sanpin(self):
        while (self.mode_combo.currentText() == "120/15"):
            device_handler.device_handler(0,0,250)
            time.sleep(7200)
            device_handler.device_handler(250,0,0)
            time.sleep(900)

    def fif(self):
        while (self.mode_combo.currentText() == "45/15"):
            device_handler.device_handler(250,0,0)
            time.sleep(2700)
            device_handler.device_handler(0,250,0)
            time.sleep(900)

    
        #     if  self.status_combo.currentTextChanged.connect(self.onCurrentStatusChanged)
        # self.mode_combo.currentTextChanged.connect(self.onCurrentModeChanged)
    
    def closeEvent(self, event):

        reply = QtWidgets.QMessageBox.question(self, 'Выйти',
            "Выключить кристалл?", QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            device_handler.device_handler(0,0,0)
            event.accept()
        else:
            event.ignore()
    
    def notice_to_label(self, text):
        if text == "404":
            self.warning_label.setText("Устройство не обнаружено")
        else:
            self.warning_label.setText("")


    def retranslateUi(self, SWW):
        _translate = QtCore.QCoreApplication.translate
        SWW.setWindowTitle(_translate("SWW", "Поток"))
        self.status_label.setText(_translate("SWW", "Статус"))
        self.status_combo.setItemText(0, _translate("SWW", "Не выбрано"))
        self.status_combo.setItemText(1, _translate("SWW", "Свободна"))
        self.status_combo.setItemText(2, _translate("SWW", "Занята"))
        self.status_combo.setItemText(3, _translate("SWW", "Совещание"))
        self.status_combo.setItemText(4, _translate("SWW", "Не подходить!"))
        self.status_combo.setItemText(5, _translate("SWW", "Мозговой штурм"))
        self.status_combo.setItemText(6, _translate("SWW", "Не работаю"))
        self.mode_label.setText(_translate("SWW", "Режим"))
        self.R_label.setText(_translate("SWW", "R"))
        self.G_label.setText(_translate("SWW", "G"))
        self.B_label.setText(_translate("SWW", "B"))


def move2RightBottomCorner(win):
    screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
    screen_size = (screen_geometry.width(), screen_geometry.height())
    win_size = (win.frameSize().width(), win.frameSize().height())
    x = screen_size[0] - win_size[0]
    y = screen_size[1] - win_size[1]
    win.move(x, y)



# if __name__ == "__main__":
    
#     app = QtWidgets.QApplication(sys.argv)
#     SWW = QtWidgets.QWidget()
#     ui = Ui_SWW()
#     ui.setupUi(SWW)
#     # SWW.move(SWW.width() * -3, 0)
#     # SWW.show()
#     # device_handler.device_handler(0,0,0)
#     # move2RightBottomCorner(SWW)

#     ex = Ui_SWW()
#     sys.exit(app.exec_())
