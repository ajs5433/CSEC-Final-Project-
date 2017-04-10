import sys
from PyQt4 import QtGui
sys.path.append("A:/Desktop/myProject/Python/UI forms")
from mainWindow import Ui_MainWindow
from createUserWindow import Ui_createUserWindow

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
createUserWindow = QtGui.QWidget()

main_window = Ui_MainWindow()
create_user_window = Ui_createUserWindow()

class passwordGenerator():
    def __init__(self):
        main_window.setupUi(MainWindow)
        create_user_window.setupUi(createUserWindow)
        

        # createUserWindow.show()

    def openWindow(self):
        MainWindow.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    myApp = passwordGenerator()
    myApp.openWindow()