# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(363, 412)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.frame = QtGui.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(40, 60, 261, 301))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.createNewPassword_btn = QtGui.QPushButton(self.frame)
        self.createNewPassword_btn.setGeometry(QtCore.QRect(40, 30, 191, 61))
        self.createNewPassword_btn.setObjectName(_fromUtf8("createNewPassword_btn"))
        self.confirmPasswordCreated_btn = QtGui.QPushButton(self.frame)
        self.confirmPasswordCreated_btn.setGeometry(QtCore.QRect(40, 210, 191, 61))
        self.confirmPasswordCreated_btn.setObjectName(_fromUtf8("confirmPasswordCreated_btn"))
        self.createNewPassword_btn_2 = QtGui.QPushButton(self.frame)
        self.createNewPassword_btn_2.setGeometry(QtCore.QRect(40, 120, 191, 61))
        self.createNewPassword_btn_2.setObjectName(_fromUtf8("createNewPassword_btn_2"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.createNewPassword_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>For passwords easier to remember, but less secure compared to the Medium.</p></body></html>", None))
        self.createNewPassword_btn.setText(_translate("MainWindow", "Create new Password (Normal)", None))
        self.confirmPasswordCreated_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>To test your memory loading a created password</p></body></html>", None))
        self.confirmPasswordCreated_btn.setText(_translate("MainWindow", "Confirm Password Created", None))
        self.createNewPassword_btn_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>For stronger passwords, but more difficult to remember</p></body></html>", None))
        self.createNewPassword_btn_2.setText(_translate("MainWindow", "Create new Password (Medium)", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

