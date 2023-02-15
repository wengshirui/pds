# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(947, 535)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.city = QtWidgets.QLabel(Dialog)
        self.city.setObjectName("city")
        self.gridLayout.addWidget(self.city, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 4)
        self.queryBtn = QtWidgets.QPushButton(Dialog)
        self.queryBtn.setObjectName("queryBtn")
        self.gridLayout.addWidget(self.queryBtn, 3, 2, 1, 1)
        self.clearBtn = QtWidgets.QPushButton(Dialog)
        self.clearBtn.setObjectName("clearBtn")
        self.gridLayout.addWidget(self.clearBtn, 3, 3, 1, 1)

        self.retranslateUi(Dialog)
        self.queryBtn.clicked.connect(Dialog.queryWeather)
        self.clearBtn.clicked.connect(Dialog.clearText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "城市天气预报"))
        self.city.setText(_translate("Dialog", "城市"))
        self.comboBox.setItemText(0, _translate("Dialog", "北京"))
        self.comboBox.setItemText(1, _translate("Dialog", "南京"))
        self.comboBox.setItemText(2, _translate("Dialog", "上海"))
        self.queryBtn.setText(_translate("Dialog", "查询"))
        self.clearBtn.setText(_translate("Dialog", "清空"))

