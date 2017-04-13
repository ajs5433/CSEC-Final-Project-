# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numberWindow.ui'
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

class Ui_numberWindow(object):
    def setupUi(self, numberWindow):
        numberWindow.setObjectName(_fromUtf8("numberWindow"))
        numberWindow.resize(607, 251)
        self.next_btn = QtGui.QPushButton(numberWindow)
        self.next_btn.setGeometry(QtCore.QRect(490, 190, 81, 31))
        self.next_btn.setObjectName(_fromUtf8("next_btn"))
        self.number1_label = QtGui.QLabel(numberWindow)
        self.number1_label.setGeometry(QtCore.QRect(40, 50, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.number1_label.setFont(font)
        self.number1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.number1_label.setObjectName(_fromUtf8("number1_label"))
        self.operation_label = QtGui.QLabel(numberWindow)
        self.operation_label.setGeometry(QtCore.QRect(130, 50, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.operation_label.setFont(font)
        self.operation_label.setText(_fromUtf8(""))
        self.operation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.operation_label.setObjectName(_fromUtf8("operation_label"))
        self.number2_label = QtGui.QLabel(numberWindow)
        self.number2_label.setGeometry(QtCore.QRect(220, 50, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.number2_label.setFont(font)
        self.number2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.number2_label.setObjectName(_fromUtf8("number2_label"))
        self.equal_label = QtGui.QLabel(numberWindow)
        self.equal_label.setGeometry(QtCore.QRect(310, 50, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.equal_label.setFont(font)
        self.equal_label.setText(_fromUtf8(""))
        self.equal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_label.setObjectName(_fromUtf8("equal_label"))
        self.result_label = QtGui.QLabel(numberWindow)
        self.result_label.setGeometry(QtCore.QRect(400, 50, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.result_label.setFont(font)
        self.result_label.setText(_fromUtf8(""))
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName(_fromUtf8("result_label"))
        self.wholenumber_le = QtGui.QLineEdit(numberWindow)
        self.wholenumber_le.setGeometry(QtCore.QRect(360, 190, 113, 31))
        self.wholenumber_le.setObjectName(_fromUtf8("wholenumber_le"))
        self.label = QtGui.QLabel(numberWindow)
        self.label.setGeometry(QtCore.QRect(70, 200, 281, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(numberWindow)
        QtCore.QMetaObject.connectSlotsByName(numberWindow)

    def retranslateUi(self, numberWindow):
        numberWindow.setWindowTitle(_translate("numberWindow", "Remember your number!", None))
        self.next_btn.setText(_translate("numberWindow", "Next", None))
        self.number1_label.setText(_translate("numberWindow", "8", None))
        self.number2_label.setText(_translate("numberWindow", "8", None))
        self.label.setText(_translate("numberWindow", "Write your whole generated pin number:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    numberWindow = QtGui.QWidget()
    ui = Ui_numberWindow()
    ui.setupUi(numberWindow)
    numberWindow.show()
    sys.exit(app.exec_())

