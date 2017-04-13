# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
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

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName(_fromUtf8("loginWindow"))
        loginWindow.resize(484, 345)
        self.ok_btn = QtGui.QPushButton(loginWindow)
        self.ok_btn.setGeometry(QtCore.QRect(360, 270, 51, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_btn.sizePolicy().hasHeightForWidth())
        self.ok_btn.setSizePolicy(sizePolicy)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.label = QtGui.QLabel(loginWindow)
        self.label.setGeometry(QtCore.QRect(60, 130, 31, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(loginWindow)
        self.label_2.setGeometry(QtCore.QRect(230, 130, 61, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(loginWindow)
        self.label_3.setGeometry(QtCore.QRect(190, 230, 81, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.passwordType_cb = QtGui.QComboBox(loginWindow)
        self.passwordType_cb.setGeometry(QtCore.QRect(290, 230, 121, 22))
        self.passwordType_cb.setObjectName(_fromUtf8("passwordType_cb"))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.passwordType_cb.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(loginWindow)
        self.label_4.setGeometry(QtCore.QRect(160, 50, 161, 31))
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
        self.name_le = QtGui.QLineEdit(loginWindow)
        self.name_le.setGeometry(QtCore.QRect(100, 130, 113, 20))
        self.name_le.setObjectName(_fromUtf8("name_le"))
        self.lastName_le = QtGui.QLineEdit(loginWindow)
        self.lastName_le.setGeometry(QtCore.QRect(300, 130, 113, 20))
        self.lastName_le.setObjectName(_fromUtf8("lastName_le"))
        self.password_le = QtGui.QLineEdit(loginWindow)
        self.password_le.setGeometry(QtCore.QRect(100, 180, 131, 20))
        self.password_le.setEchoMode(QtGui.QLineEdit.Password)
        self.password_le.setObjectName(_fromUtf8("password_le"))
        self.label_6 = QtGui.QLabel(loginWindow)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 81, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.showPassword_cb = QtGui.QCheckBox(loginWindow)
        self.showPassword_cb.setGeometry(QtCore.QRect(300, 180, 101, 21))
        self.showPassword_cb.setObjectName(_fromUtf8("showPassword_cb"))

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(_translate("loginWindow", "Log in", None))
        self.ok_btn.setText(_translate("loginWindow", "Ok", None))
        self.ok_btn.setShortcut(_translate("loginWindow", "Return", None))
        self.label.setText(_translate("loginWindow", "Name:", None))
        self.label_2.setText(_translate("loginWindow", "Last Name:", None))
        self.label_3.setText(_translate("loginWindow", "Password Type:", None))
        self.passwordType_cb.setToolTip(_translate("loginWindow", "<html><head/><body><p>Please <span style=\" font-weight:600;\">DO</span><span style=\" font-weight:600;\">NOT</span> select <span style=\" font-style:italic;\">&lt;Not this one&gt;. </span>This was created to test the application ONLY and the results will not be considered.</p></body></html>", None))
        self.passwordType_cb.setItemText(0, _translate("loginWindow", "-set password type-", None))
        self.passwordType_cb.setItemText(1, _translate("loginWindow", "Testing Password 1", None))
        self.passwordType_cb.setItemText(2, _translate("loginWindow", "Testing Password 2", None))
        self.passwordType_cb.setItemText(3, _translate("loginWindow", "Testing Password 3", None))
        self.passwordType_cb.setItemText(4, _translate("loginWindow", "Gmail", None))
        self.passwordType_cb.setItemText(5, _translate("loginWindow", "Facebook", None))
        self.passwordType_cb.setItemText(6, _translate("loginWindow", "Slack", None))
        self.passwordType_cb.setItemText(7, _translate("loginWindow", "<Not this one>", None))
        self.label_4.setText(_translate("loginWindow", "Welcome back!!", None))
        self.label_6.setText(_translate("loginWindow", "Password:", None))
        self.showPassword_cb.setText(_translate("loginWindow", "Show Password", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    loginWindow = QtGui.QWidget()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())

