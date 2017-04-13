# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculateNumbers.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_calculateNumbersWindow(object):
    def setupUi(self, calculateNumbersWindow):
        calculateNumbersWindow.setObjectName(_fromUtf8("calculateNumbersWindow"))
        calculateNumbersWindow.resize(599, 262)
        self.label = QtGui.QLabel(calculateNumbersWindow)
        self.label.setGeometry(QtCore.QRect(50, 20, 491, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(calculateNumbersWindow)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 501, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(calculateNumbersWindow)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.number1_le = QtGui.QLineEdit(calculateNumbersWindow)
        self.number1_le.setGeometry(QtCore.QRect(160, 140, 31, 20))
        self.number1_le.setObjectName(_fromUtf8("number1_le"))
        self.label_4 = QtGui.QLabel(calculateNumbersWindow)
        self.label_4.setGeometry(QtCore.QRect(100, 170, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.number2_le = QtGui.QLineEdit(calculateNumbersWindow)
        self.number2_le.setGeometry(QtCore.QRect(160, 170, 31, 20))
        self.number2_le.setObjectName(_fromUtf8("number2_le"))
        self.label_5 = QtGui.QLabel(calculateNumbersWindow)
        self.label_5.setGeometry(QtCore.QRect(100, 200, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.results_le = QtGui.QLineEdit(calculateNumbersWindow)
        self.results_le.setGeometry(QtCore.QRect(160, 200, 31, 20))
        self.results_le.setObjectName(_fromUtf8("results_le"))
        self.ok_btn = QtGui.QPushButton(calculateNumbersWindow)
        self.ok_btn.setGeometry(QtCore.QRect(480, 180, 51, 31))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))

        self.retranslateUi(calculateNumbersWindow)
        QtCore.QMetaObject.connectSlotsByName(calculateNumbersWindow)

    def retranslateUi(self, calculateNumbersWindow):
        calculateNumbersWindow.setWindowTitle(_translate("calculateNumbersWindow", "Calculate your numbers", None))
        self.label.setText(_translate("calculateNumbersWindow", "We have assigned two random numbers to you and you will need to do a simple random operation with them.", None))
        self.label_2.setText(_translate("calculateNumbersWindow", "your numbers are x and y, you will need to...", None))
        self.label_3.setText(_translate("calculateNumbersWindow", "Number 1", None))
        self.label_4.setText(_translate("calculateNumbersWindow", "Number 1", None))
        self.label_5.setText(_translate("calculateNumbersWindow", "Result", None))
        self.ok_btn.setText(_translate("calculateNumbersWindow", "Ok", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    calculateNumbersWindow = QtGui.QWidget()
    ui = Ui_calculateNumbersWindow()
    ui.setupUi(calculateNumbersWindow)
    calculateNumbersWindow.show()
    sys.exit(app.exec_())

