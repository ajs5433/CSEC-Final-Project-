# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createUserWindow.ui'
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

class Ui_createUserWindow(object):
    def setupUi(self, createUserWindow):
        createUserWindow.setObjectName(_fromUtf8("createUserWindow"))
        createUserWindow.resize(267, 365)
        self.ok_btn = QtGui.QPushButton(createUserWindow)
        self.ok_btn.setGeometry(QtCore.QRect(180, 310, 41, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_btn.sizePolicy().hasHeightForWidth())
        self.ok_btn.setSizePolicy(sizePolicy)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.label = QtGui.QLabel(createUserWindow)
        self.label.setGeometry(QtCore.QRect(70, 140, 31, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(createUserWindow)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 61, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(createUserWindow)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 81, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.passwordType_cb = QtGui.QComboBox(createUserWindow)
        self.passwordType_cb.setGeometry(QtCore.QRect(110, 240, 121, 22))
        self.passwordType_cb.setObjectName(_fromUtf8("passwordType_cb"))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(createUserWindow)
        self.label_4.setGeometry(QtCore.QRect(60, 50, 161, 31))
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setLineWidth(1)
        self.label_4.setMidLineWidth(0)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(createUserWindow)
        self.label_5.setGeometry(QtCore.QRect(60, 80, 161, 31))
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setLineWidth(1)
        self.label_5.setMidLineWidth(0)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.name_le = QtGui.QLineEdit(createUserWindow)
        self.name_le.setGeometry(QtCore.QRect(110, 140, 121, 20))
        self.name_le.setObjectName(_fromUtf8("name_le"))
        self.lastName_le = QtGui.QLineEdit(createUserWindow)
        self.lastName_le.setGeometry(QtCore.QRect(110, 190, 121, 20))
        self.lastName_le.setObjectName(_fromUtf8("lastName_le"))

        self.retranslateUi(createUserWindow)
        QtCore.QMetaObject.connectSlotsByName(createUserWindow)

    def retranslateUi(self, createUserWindow):
        createUserWindow.setWindowTitle(_translate("createUserWindow", "Create User", None))
        self.ok_btn.setText(_translate("createUserWindow", "Ok", None))
        self.ok_btn.setShortcut(_translate("createUserWindow", "Return", None))
        self.label.setText(_translate("createUserWindow", "Name:", None))
        self.label_2.setText(_translate("createUserWindow", "Last Name:", None))
        self.label_3.setText(_translate("createUserWindow", "Password Type:", None))
        self.passwordType_cb.setItemText(0, _translate("createUserWindow", "-set password type-", None))
        self.passwordType_cb.setItemText(1, _translate("createUserWindow", "Testing Password 1", None))
        self.passwordType_cb.setItemText(2, _translate("createUserWindow", "Testing Password 2", None))
        self.passwordType_cb.setItemText(3, _translate("createUserWindow", "Testing Password 3", None))
        self.passwordType_cb.setItemText(4, _translate("createUserWindow", "Gmail", None))
        self.passwordType_cb.setItemText(5, _translate("createUserWindow", "Facebook", None))
        self.passwordType_cb.setItemText(6, _translate("createUserWindow", "Slack", None))
        self.label_4.setText(_translate("createUserWindow", "Welcome", None))
        self.label_5.setText(_translate("createUserWindow", "Welcome", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    createUserWindow = QtGui.QWidget()
    ui = Ui_createUserWindow()
    ui.setupUi(createUserWindow)
    createUserWindow.show()
    sys.exit(app.exec_())

