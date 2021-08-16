from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_H(object):
    def setupUi(self, H):
        H.setObjectName("H")
        H.resize(569, 600)
        self.centralwidget = QtWidgets.QWidget(H)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 370, 501, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 36, 481, 271))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        H.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(H)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 22))
        self.menubar.setObjectName("menubar")
        H.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(H)
        self.statusbar.setObjectName("statusbar")
        H.setStatusBar(self.statusbar)
        self.retranslateUi(H)
        self.pushButton.clicked.connect(lambda: self.label.setText('han is de man'))
        QtCore.QMetaObject.connectSlotsByName(H)

    def retranslateUi(self, H):
        _translate = QtCore.QCoreApplication.translate
        H.setWindowTitle(_translate("H", "HSK VOCABULARY"))
        self.pushButton.setText(_translate("H", "NEXT"))
        self.label.setText(_translate("H", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    H = QtWidgets.QMainWindow()
    ui = Ui_H()
    ui.setupUi(H)
    H.show()
    sys.exit(app.exec_())
