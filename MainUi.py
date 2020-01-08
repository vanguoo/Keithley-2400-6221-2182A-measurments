# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2400pulse_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *

class Ui_Form(object):
    

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(398, 321)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(13)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 30, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.SRC_I = QtWidgets.QPushButton(Form)
        self.SRC_I.setGeometry(QtCore.QRect(110, 90, 171, 61))
        self.SRC_I.setCheckable(False)
        self.SRC_I.setObjectName("SRC_I")
        self.SRC_V = QtWidgets.QPushButton(Form)
        self.SRC_V.setGeometry(QtCore.QRect(110, 170, 171, 61))
        self.SRC_V.setCheckable(False)
        self.SRC_V.setObjectName("SRC_V")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Welcome! Here is 2400-PulseMode"))
        self.SRC_I.setText(_translate("Form", "Source I Mesure V"))
        self.SRC_V.setText(_translate("Form", "Source V Mesure I"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
