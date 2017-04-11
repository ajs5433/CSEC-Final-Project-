import sys
sys.path.append("A:/Desktop/myProject/Python/UI forms")
from myExcel import myExcel
from myGUI import myGUI
from PyQt4 import QtGui
from PyQt4 import QtCore
from charWindow import Ui_characterWindow
from login import Ui_login
from mainWindow import Ui_MainWindow

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
characterWindow = QtGui.QWidget()
login = QtGui.QWidget()
mw = Ui_MainWindow()
li = Ui_login()
cw = Ui_characterWindow()


class WindowController():
    def login(self):
        print("test")

    def openWindow(self):

        mw.setupUi(MainWindow)

        li.setupUi(login)

        cw.setupUi(characterWindow)

        mw.pushButton.clicked.connect(self.login)
        li.pushButton.clicked.connect(self.characterSelect)

        # characterWindow.show()
        # login.show()
        MainWindow.show()

        sys.exit(app.exec_())

    def login(self):
        print("Button Pushed")
        MainWindow.close();
        login.show();

    def characterSelect(self):
        MainWindow.close()
        characterWindow.show()
        login.close()

        maria = QtCore.QSize(50,50)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic1.jpg"))
        cw.btn_1.setIcon(icon)
        cw.btn_1.setIconSize(maria)
        cw.btn_2.setIcon(QtGui.QIcon('pic2.jpg'))
        cw.btn_2.setIconSize(maria)
        cw.btn_3.setIcon(QtGui.QIcon('pic3.jpg'))
        cw.btn_3.setIconSize(maria)

if __name__ == "__main__":
    window = WindowController()
    window.openWindow()