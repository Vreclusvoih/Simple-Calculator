# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(310, 296)
        widget.setMaximumSize(QtCore.QSize(397, 420))
        widget.setStyleSheet("QWidget\n"
"{\n"
"background-color:rgb(39, 37, 35);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.multiplicationButton = QtWidgets.QPushButton(widget)
        self.multiplicationButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.multiplicationButton.setObjectName("multiplicationButton")
        self.gridLayout.addWidget(self.multiplicationButton, 8, 4, 1, 1)
        self.zeroButton = QtWidgets.QPushButton(widget)
        self.zeroButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.zeroButton.setObjectName("zeroButton")
        self.gridLayout.addWidget(self.zeroButton, 10, 2, 1, 1)
        self.threeButton = QtWidgets.QPushButton(widget)
        self.threeButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.threeButton.setObjectName("threeButton")
        self.gridLayout.addWidget(self.threeButton, 4, 3, 1, 1)
        self.delLastSymbolButton = QtWidgets.QPushButton(widget)
        self.delLastSymbolButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 183, 15);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size: 20px;\n"
"}")
        self.delLastSymbolButton.setObjectName("delLastSymbolButton")
        self.gridLayout.addWidget(self.delLastSymbolButton, 3, 1, 1, 1)
        self.degreeButton = QtWidgets.QPushButton(widget)
        self.degreeButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.degreeButton.setObjectName("degreeButton")
        self.gridLayout.addWidget(self.degreeButton, 5, 0, 1, 1)
        self.plusButton = QtWidgets.QPushButton(widget)
        self.plusButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.plusButton.setObjectName("plusButton")
        self.gridLayout.addWidget(self.plusButton, 5, 4, 1, 1)
        self.openBracketButton = QtWidgets.QPushButton(widget)
        self.openBracketButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.openBracketButton.setObjectName("openBracketButton")
        self.gridLayout.addWidget(self.openBracketButton, 3, 2, 1, 1)
        self.eightButon = QtWidgets.QPushButton(widget)
        self.eightButon.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.eightButon.setObjectName("eightButon")
        self.gridLayout.addWidget(self.eightButon, 8, 2, 1, 1)
        self.rootOfButton = QtWidgets.QPushButton(widget)
        self.rootOfButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.rootOfButton.setObjectName("rootOfButton")
        self.gridLayout.addWidget(self.rootOfButton, 4, 0, 1, 1)
        self.dotButton = QtWidgets.QPushButton(widget)
        self.dotButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.dotButton.setObjectName("dotButton")
        self.gridLayout.addWidget(self.dotButton, 10, 3, 1, 1)
        self.nineButton = QtWidgets.QPushButton(widget)
        self.nineButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.nineButton.setObjectName("nineButton")
        self.gridLayout.addWidget(self.nineButton, 8, 3, 1, 1)
        self.oneButton = QtWidgets.QPushButton(widget)
        self.oneButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.oneButton.setObjectName("oneButton")
        self.gridLayout.addWidget(self.oneButton, 4, 1, 1, 1)
        self.eButton = QtWidgets.QPushButton(widget)
        self.eButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.eButton.setObjectName("eButton")
        self.gridLayout.addWidget(self.eButton, 10, 1, 1, 1)
        self.oneOfButton = QtWidgets.QPushButton(widget)
        self.oneOfButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.oneOfButton.setObjectName("oneOfButton")
        self.gridLayout.addWidget(self.oneOfButton, 8, 0, 1, 1)
        self.sixButton = QtWidgets.QPushButton(widget)
        self.sixButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.sixButton.setObjectName("sixButton")
        self.gridLayout.addWidget(self.sixButton, 5, 3, 1, 1)
        self.fifeButton = QtWidgets.QPushButton(widget)
        self.fifeButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.fifeButton.setObjectName("fifeButton")
        self.gridLayout.addWidget(self.fifeButton, 5, 2, 1, 1)
        self.equalsButton = QtWidgets.QPushButton(widget)
        self.equalsButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"color:rgb(255, 183, 15);\n"
"}")
        self.equalsButton.setObjectName("equalsButton")
        self.gridLayout.addWidget(self.equalsButton, 10, 4, 1, 1)
        self.divisionButton = QtWidgets.QPushButton(widget)
        self.divisionButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"selection-background-color: blue;\n"
"}")
        self.divisionButton.setObjectName("divisionButton")
        self.gridLayout.addWidget(self.divisionButton, 3, 4, 1, 1)
        self.sevenButton = QtWidgets.QPushButton(widget)
        self.sevenButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.sevenButton.setObjectName("sevenButton")
        self.gridLayout.addWidget(self.sevenButton, 8, 1, 1, 1)
        self.minusButton = QtWidgets.QPushButton(widget)
        self.minusButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.minusButton.setObjectName("minusButton")
        self.gridLayout.addWidget(self.minusButton, 4, 4, 1, 1)
        self.twoButton = QtWidgets.QPushButton(widget)
        self.twoButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.twoButton.setObjectName("twoButton")
        self.gridLayout.addWidget(self.twoButton, 4, 2, 1, 1)
        self.closeBracketButton = QtWidgets.QPushButton(widget)
        self.closeBracketButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)\n"
";min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.closeBracketButton.setObjectName("closeBracketButton")
        self.gridLayout.addWidget(self.closeBracketButton, 3, 3, 1, 1)
        self.fourButton = QtWidgets.QPushButton(widget)
        self.fourButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.fourButton.setObjectName("fourButton")
        self.gridLayout.addWidget(self.fourButton, 5, 1, 1, 1)
        self.PiButton = QtWidgets.QPushButton(widget)
        self.PiButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.PiButton.setObjectName("PiButton")
        self.gridLayout.addWidget(self.PiButton, 10, 0, 1, 1)
        self.delAllButton = QtWidgets.QPushButton(widget)
        self.delAllButton.setStyleSheet("QPushButton\n"
"{\n"
"border: 2px solid rgb(255, 203, 15);\n"
"border-radius: 20px;\n"
"color:rgb(255, 183, 15);\n"
"background-color:rgb(0, 0, 0);\n"
"min-width: 40px;\n"
"min-height:40px;\n"
"padding:0;\n"
"font-size:15px;\n"
"}")
        self.delAllButton.setObjectName("delAllButton")
        self.gridLayout.addWidget(self.delAllButton, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(widget)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"background-color:rgb(61, 59, 57);\n"
"font-size: 20px;\n"
"font: 16pt \"Palatino Linotype\";\n"
"border:10px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 5)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)
        widget.setTabOrder(self.delAllButton, self.delLastSymbolButton)
        widget.setTabOrder(self.delLastSymbolButton, self.openBracketButton)
        widget.setTabOrder(self.openBracketButton, self.closeBracketButton)
        widget.setTabOrder(self.closeBracketButton, self.divisionButton)
        widget.setTabOrder(self.divisionButton, self.rootOfButton)
        widget.setTabOrder(self.rootOfButton, self.oneButton)
        widget.setTabOrder(self.oneButton, self.twoButton)
        widget.setTabOrder(self.twoButton, self.threeButton)
        widget.setTabOrder(self.threeButton, self.minusButton)
        widget.setTabOrder(self.minusButton, self.degreeButton)
        widget.setTabOrder(self.degreeButton, self.fourButton)
        widget.setTabOrder(self.fourButton, self.fifeButton)
        widget.setTabOrder(self.fifeButton, self.sixButton)
        widget.setTabOrder(self.sixButton, self.plusButton)
        widget.setTabOrder(self.plusButton, self.oneOfButton)
        widget.setTabOrder(self.oneOfButton, self.sevenButton)
        widget.setTabOrder(self.sevenButton, self.eightButon)
        widget.setTabOrder(self.eightButon, self.nineButton)
        widget.setTabOrder(self.nineButton, self.multiplicationButton)
        widget.setTabOrder(self.multiplicationButton, self.PiButton)
        widget.setTabOrder(self.PiButton, self.eButton)
        widget.setTabOrder(self.eButton, self.zeroButton)
        widget.setTabOrder(self.zeroButton, self.dotButton)
        widget.setTabOrder(self.dotButton, self.equalsButton)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "DIB_Calculator"))
        self.multiplicationButton.setText(_translate("widget", "x"))
        self.zeroButton.setText(_translate("widget", "0"))
        self.threeButton.setText(_translate("widget", "3"))
        self.delLastSymbolButton.setText(_translate("widget", "←"))
        self.degreeButton.setText(_translate("widget", "x^"))
        self.plusButton.setText(_translate("widget", "+"))
        self.openBracketButton.setText(_translate("widget", "("))
        self.eightButon.setText(_translate("widget", "8"))
        self.rootOfButton.setText(_translate("widget", "√x"))
        self.dotButton.setText(_translate("widget", "."))
        self.nineButton.setText(_translate("widget", "9"))
        self.oneButton.setText(_translate("widget", "1"))
        self.eButton.setText(_translate("widget", "e"))
        self.oneOfButton.setText(_translate("widget", "1/x"))
        self.sixButton.setText(_translate("widget", "6"))
        self.fifeButton.setText(_translate("widget", "5"))
        self.equalsButton.setText(_translate("widget", "="))
        self.divisionButton.setText(_translate("widget", "/"))
        self.sevenButton.setText(_translate("widget", "7"))
        self.minusButton.setText(_translate("widget", "–"))
        self.twoButton.setText(_translate("widget", "2"))
        self.closeBracketButton.setText(_translate("widget", ")"))
        self.fourButton.setText(_translate("widget", "4"))
        self.PiButton.setText(_translate("widget", "Pi"))
        self.delAllButton.setText(_translate("widget", "AC"))
        self.label.setText(_translate("widget", ""))

