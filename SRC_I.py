# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SRC_I.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

class Ui_Dialog(object):


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(511, 384)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(115, 57, 274, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dir = QtWidgets.QLineEdit(self.layoutWidget)
        self.dir.setObjectName("dir")
        self.gridLayout.addWidget(self.dir, 1, 0, 1, 1)
        self.filename = QtWidgets.QLineEdit(self.layoutWidget)
        self.filename.setObjectName("filename")
        self.gridLayout.addWidget(self.filename, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 119, 402, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.high = QtWidgets.QLineEdit(self.layoutWidget1)
        self.high.setObjectName("high")
        self.gridLayout_2.addWidget(self.high, 1, 1, 1, 1)
        self.low = QtWidgets.QLineEdit(self.layoutWidget1)
        self.low.setObjectName("low")
        self.gridLayout_2.addWidget(self.low, 1, 2, 1, 1)
        self.compliance = QtWidgets.QLineEdit(self.layoutWidget1)
        self.compliance.setObjectName("compliance")
        self.gridLayout_2.addWidget(self.compliance, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        self.width = QtWidgets.QLineEdit(self.layoutWidget1)
        self.width.setObjectName("width")
        self.gridLayout_2.addWidget(self.width, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.confirm = QtWidgets.QPushButton(Dialog)
        self.confirm.setGeometry(QtCore.QRect(60, 270, 400, 23))
        self.confirm.setObjectName("confirm")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(60, 310, 400, 23))
        self.start.setObjectName("start")
        self.period = QtWidgets.QLineEdit(Dialog)
        self.period.setGeometry(QtCore.QRect(60, 210, 95, 20))
        self.period.setObjectName("period")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(60, 190, 91, 16))
        self.label_8.setObjectName("label_8")
        self.inreasing = QtWidgets.QRadioButton(Dialog)
        self.inreasing.setGeometry(QtCore.QRect(270, 210, 89, 16))
        self.inreasing.setObjectName("inreasing")
        self.rate = QtWidgets.QSpinBox(Dialog)
        self.rate.setGeometry(QtCore.QRect(370, 210, 42, 22))
        self.rate.setObjectName("rate")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(373, 196, 54, 12))
        self.label_9.setObjectName("label_9")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(220, 350, 75, 23))
        self.back.setObjectName("stop")
        self.label_6.setBuddy(self.dir)
        self.label_7.setBuddy(self.filename)
        self.label_4.setBuddy(self.width)
        self.label.setBuddy(self.high)
        self.label_5.setBuddy(self.compliance)
        self.label_2.setBuddy(self.low)
        self.label_8.setBuddy(self.period)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.dir, self.filename)
        Dialog.setTabOrder(self.filename, self.high)
        Dialog.setTabOrder(self.high, self.low)
        Dialog.setTabOrder(self.low, self.width)
        Dialog.setTabOrder(self.width, self.compliance)
        Dialog.setTabOrder(self.compliance, self.period)
        Dialog.setTabOrder(self.period, self.inreasing)
        Dialog.setTabOrder(self.inreasing, self.rate)
        Dialog.setTabOrder(self.rate, self.confirm)
        Dialog.setTabOrder(self.confirm, self.start)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SourceI_MeasureV"))
        self.label_6.setText(_translate("Dialog", "FileDir"))
        self.label_7.setText(_translate("Dialog", "FileName"))
        self.label_4.setText(_translate("Dialog", "Width"))
        self.label.setText(_translate("Dialog", "High"))
        self.label_5.setText(_translate("Dialog", "Compliance"))
        self.label_2.setText(_translate("Dialog", "Low"))
        self.confirm.setText(_translate("Dialog", "Confirm Input"))
        self.start.setText(_translate("Dialog", "START!"))
        self.label_8.setText(_translate("Dialog", "Period Number"))
        self.inreasing.setText(_translate("Dialog", "Increasing?"))
        self.label_9.setText(_translate("Dialog", "Rate"))
        self.back.setText(_translate("Dialog", "stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())