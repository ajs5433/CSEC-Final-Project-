import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import QObject

from myExcel import myExcel
sys.path.append("A:/Desktop/myProject/Python/UI forms")
from mainWindow import Ui_MainWindow
from createUserWindow import Ui_createUserWindow
from loginWindow import Ui_loginWindow
from selectCharacterWindow import Ui_characterWindow

xlsheet = myExcel()
imagesPath = "A:/Desktop/myProject/Project Files/Images/"
buttonName = ""

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
createUserWindow = QtGui.QWidget()
loginWindow = QtGui.QWidget()
characterWindow = QtGui.QWidget()

main_window = Ui_MainWindow()
create_user_window = Ui_createUserWindow()
login_window = Ui_loginWindow()
select_character_window = Ui_characterWindow()

class passwordGenerator(QtGui.QWidget):
    def __init__(self):
        super(passwordGenerator, self).__init__()
        main_window.setupUi(MainWindow)
        create_user_window.setupUi(createUserWindow)
        login_window.setupUi(loginWindow)
        select_character_window.setupUi(characterWindow)

    def openWindow(self):
        #MainWindow.show()
        #createUserWindow.show()
        #loginWindow.show()
        self.setupCharacterWindow()
        characterWindow.show()
        sys.exit(app.exec_())

    def setupCharacterWindow(self):
        self.setupCW(select_character_window.btn_1, 1)
        self.setupCW(select_character_window.btn_2, 2)
        self.setupCW(select_character_window.btn_3, 3)
        self.setupCW(select_character_window.btn_4, 4)
        self.setupCW(select_character_window.btn_5, 5)
        self.setupCW(select_character_window.btn_6, 6)
        self.setupCW(select_character_window.btn_7, 7)
        self.setupCW(select_character_window.btn_8, 8)
        self.setupCW(select_character_window.btn_9, 9)
        self.setupCW(select_character_window.btn_10, 10)
        self.setupCW(select_character_window.btn_11, 11)
        self.setupCW(select_character_window.btn_12, 12)
        self.setupCW(select_character_window.btn_13, 13)
        self.setupCW(select_character_window.btn_14, 14)
        self.setupCW(select_character_window.btn_15, 15)
        self.setupCW(select_character_window.btn_16, 16)
        self.setupCW(select_character_window.btn_17, 17)
        self.setupCW(select_character_window.btn_18, 18)
        self.setupCW(select_character_window.btn_19, 19)
        self.setupCW(select_character_window.btn_27, 20)
        self.setupCW(select_character_window.btn_21, 21)
        self.setupCW(select_character_window.btn_22, 22)
        self.setupCW(select_character_window.btn_23, 23)
        self.setupCW(select_character_window.btn_24, 24)
        self.setupCW(select_character_window.btn_25, 25)
        self.setupCW(select_character_window.btn_26, 26)

    def setupCW(self, button, number):
        myName = xlsheet.getRandomName(number)
        myIconSize = QtCore.QSize(81, 81)
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(imagesPath+myName+".jpg"))
        button.setIcon(myIcon)
        button.setIconSize(myIconSize)
        button.setToolTip(myName)
        button.clicked.connect(self.CWButtonPushed)
        button.setObjectName(myName)

    def CWButtonPushed(self):
        name = self.sender().objectName()
        select_character_window.name_label.setText(name)
        """
        #old method
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap(imagesPath+name+".jpg"))
        scene.setSceneRect(QtCore.QRectF(0,0,2,2))
        select_character_window.graphicsView.setScene(scene)
        """
        

if __name__ == "__main__":
    myApp = passwordGenerator()
    myApp.openWindow()