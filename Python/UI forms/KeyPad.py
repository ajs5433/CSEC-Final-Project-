# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KeyPad.ui'
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

class Ui_keyPad(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(369, 507)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(50, 110, 251, 311))
        self.frame.setStyleSheet(_fromUtf8("background: rgb(0, 170, 255)"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_3 = QtGui.QPushButton(self.frame)
        self.btn_3.setGeometry(QtCore.QRect(130, 190, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setAutoFillBackground(False)
        self.btn_3.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.btn_13 = QtGui.QPushButton(self.frame)
        self.btn_13.setGeometry(QtCore.QRect(190, 70, 51, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_13.setFont(font)
        self.btn_13.setAutoFillBackground(False)
        self.btn_13.setStyleSheet(_fromUtf8("background: rgb(220, 255, 60)"))
        self.btn_13.setObjectName(_fromUtf8("btn_13"))
        self.btn_12 = QtGui.QPushButton(self.frame)
        self.btn_12.setGeometry(QtCore.QRect(190, 190, 51, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_12.setFont(font)
        self.btn_12.setAutoFillBackground(False)
        self.btn_12.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_12.setObjectName(_fromUtf8("btn_12"))
        self.btn_7 = QtGui.QPushButton(self.frame)
        self.btn_7.setGeometry(QtCore.QRect(10, 70, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setAutoFillBackground(False)
        self.btn_7.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_7.setObjectName(_fromUtf8("btn_7"))
        self.btn_15 = QtGui.QPushButton(self.frame)
        self.btn_15.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_15.setFont(font)
        self.btn_15.setAutoFillBackground(False)
        self.btn_15.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_15.setText(_fromUtf8(""))
        self.btn_15.setObjectName(_fromUtf8("btn_15"))
        self.btn_8 = QtGui.QPushButton(self.frame)
        self.btn_8.setGeometry(QtCore.QRect(70, 70, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setAutoFillBackground(False)
        self.btn_8.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_8.setObjectName(_fromUtf8("btn_8"))
        self.btn_1 = QtGui.QPushButton(self.frame)
        self.btn_1.setGeometry(QtCore.QRect(10, 190, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setAutoFillBackground(False)
        self.btn_1.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.btn_6 = QtGui.QPushButton(self.frame)
        self.btn_6.setGeometry(QtCore.QRect(130, 130, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setAutoFillBackground(False)
        self.btn_6.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_6.setObjectName(_fromUtf8("btn_6"))
        self.btn_9 = QtGui.QPushButton(self.frame)
        self.btn_9.setGeometry(QtCore.QRect(130, 70, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setAutoFillBackground(False)
        self.btn_9.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_9.setObjectName(_fromUtf8("btn_9"))
        self.btn_2 = QtGui.QPushButton(self.frame)
        self.btn_2.setGeometry(QtCore.QRect(70, 190, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setAutoFillBackground(False)
        self.btn_2.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.btn_10 = QtGui.QPushButton(self.frame)
        self.btn_10.setGeometry(QtCore.QRect(10, 250, 111, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_10.setFont(font)
        self.btn_10.setAutoFillBackground(False)
        self.btn_10.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_10.setObjectName(_fromUtf8("btn_10"))
        self.btn_17 = QtGui.QPushButton(self.frame)
        self.btn_17.setGeometry(QtCore.QRect(130, 10, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_17.setFont(font)
        self.btn_17.setAutoFillBackground(False)
        self.btn_17.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_17.setObjectName(_fromUtf8("btn_17"))
        self.btn_16 = QtGui.QPushButton(self.frame)
        self.btn_16.setGeometry(QtCore.QRect(70, 10, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_16.setFont(font)
        self.btn_16.setAutoFillBackground(False)
        self.btn_16.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_16.setObjectName(_fromUtf8("btn_16"))
        self.btn_4 = QtGui.QPushButton(self.frame)
        self.btn_4.setGeometry(QtCore.QRect(10, 130, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setAutoFillBackground(False)
        self.btn_4.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_4.setObjectName(_fromUtf8("btn_4"))
        self.btn_11 = QtGui.QPushButton(self.frame)
        self.btn_11.setGeometry(QtCore.QRect(130, 250, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_11.setFont(font)
        self.btn_11.setAutoFillBackground(False)
        self.btn_11.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_11.setObjectName(_fromUtf8("btn_11"))
        self.btn_5 = QtGui.QPushButton(self.frame)
        self.btn_5.setGeometry(QtCore.QRect(70, 130, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setAutoFillBackground(False)
        self.btn_5.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_5.setObjectName(_fromUtf8("btn_5"))
        self.btn_minus = QtGui.QPushButton(self.frame)
        self.btn_minus.setGeometry(QtCore.QRect(190, 10, 51, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setAutoFillBackground(False)
        self.btn_minus.setStyleSheet(_fromUtf8("background: rgb(255, 255, 255)"))
        self.btn_minus.setObjectName(_fromUtf8("btn_minus"))
        self.btn_15.raise_()
        self.label.raise_()
        self.btn_3.raise_()
        self.btn_13.raise_()
        self.btn_12.raise_()
        self.btn_7.raise_()
        self.btn_8.raise_()
        self.btn_1.raise_()
        self.btn_6.raise_()
        self.btn_9.raise_()
        self.btn_2.raise_()
        self.btn_10.raise_()
        self.btn_17.raise_()
        self.btn_16.raise_()
        self.btn_4.raise_()
        self.btn_11.raise_()
        self.btn_5.raise_()
        self.btn_minus.raise_()
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 311, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.next_btn = QtGui.QPushButton(Form)
        self.next_btn.setGeometry(QtCore.QRect(270, 440, 71, 41))
        self.next_btn.setObjectName(_fromUtf8("next_btn"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 450, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.number_le = QtGui.QLineEdit(Form)
        self.number_le.setGeometry(QtCore.QRect(130, 450, 91, 20))
        self.number_le.setObjectName(_fromUtf8("number_le"))
        self.frame.raise_()
        self.label_2.raise_()
        self.next_btn.raise_()
        self.label_3.raise_()
        self.number_le.raise_()
        self.btn_15.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "num lock", None))
        self.btn_3.setText(_translate("Form", "3", None))
        self.btn_13.setText(_translate("Form", "+", None))
        self.btn_12.setText(_translate("Form", "enter", None))
        self.btn_7.setText(_translate("Form", "7", None))
        self.btn_8.setText(_translate("Form", "8", None))
        self.btn_1.setText(_translate("Form", "1", None))
        self.btn_6.setText(_translate("Form", "6", None))
        self.btn_9.setText(_translate("Form", "9", None))
        self.btn_2.setText(_translate("Form", "2", None))
        self.btn_10.setText(_translate("Form", "0", None))
        self.btn_17.setText(_translate("Form", "*", None))
        self.btn_16.setText(_translate("Form", "/", None))
        self.btn_4.setText(_translate("Form", "4", None))
        self.btn_11.setText(_translate("Form", ".", None))
        self.btn_5.setText(_translate("Form", "5", None))
        self.btn_minus.setText(_translate("Form", "-", None))
        self.label_2.setText(_translate("Form", "Sometimes it is easier to remember a number when we relate them to a position. For this part, look at your keypad and type again your number.", None))
        self.next_btn.setText(_translate("Form", "Next", None))
        self.label_3.setText(_translate("Form", "Your number:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
