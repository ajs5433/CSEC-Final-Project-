import sys
import re
import random
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

myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
order = ['PAO1', 'PAO2', 'Number', 'Symbol']

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
    orderSelect = 0

    def __init__(self):
        super(passwordGenerator, self).__init__()
        main_window.setupUi(MainWindow)
        create_user_window.setupUi(createUserWindow)
        login_window.setupUi(loginWindow)
        select_character_window.setupUi(characterWindow)

    def openWindow(self):
        random.shuffle(order)
        order.insert(len(order), 'complete')
        main_window.pushButton.clicked.connect(self.nextStep_event) #createNewUser_btn
        main_window.pushButton_2.clicked.connect(self.confirmPasswordCreated_event)  # confirmPasswordCreated_btn
        MainWindow.show()
        #createUserWindow.show()
        #loginWindow.show()
        sys.exit(app.exec_())

    def setupCharacterWindow(self):
        random.shuffle(myList)
        self.setupCW(select_character_window.btn_1, myList[1])
        self.setupCW(select_character_window.btn_2, myList[2])
        self.setupCW(select_character_window.btn_3, myList[3])
        self.setupCW(select_character_window.btn_4, myList[4])
        self.setupCW(select_character_window.btn_5, myList[5])
        self.setupCW(select_character_window.btn_6, myList[6])
        self.setupCW(select_character_window.btn_7, myList[7])
        self.setupCW(select_character_window.btn_8, myList[8])
        self.setupCW(select_character_window.btn_9, myList[9])
        self.setupCW(select_character_window.btn_10, myList[10])
        self.setupCW(select_character_window.btn_11, myList[11])
        self.setupCW(select_character_window.btn_12, myList[12])
        self.setupCW(select_character_window.btn_13, myList[13])
        self.setupCW(select_character_window.btn_14, myList[14])
        self.setupCW(select_character_window.btn_15, myList[15])
        self.setupCW(select_character_window.btn_16, myList[16])
        self.setupCW(select_character_window.btn_17, myList[17])
        self.setupCW(select_character_window.btn_18, myList[18])
        self.setupCW(select_character_window.btn_19, myList[19])
        self.setupCW(select_character_window.btn_20, myList[20])
        self.setupCW(select_character_window.btn_21, myList[21])
        self.setupCW(select_character_window.btn_22, myList[22])
        self.setupCW(select_character_window.btn_23, myList[23])
        self.setupCW(select_character_window.btn_24, myList[24])
        self.setupCW(select_character_window.btn_25, myList[25])
        self.setupCW(select_character_window.btn_26, myList[0])

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
        password = ""

        for i in name.split():
            password += i[0]

        select_character_window.password_label.setText(password)

        # print(re.findall()
        """
        #old method
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap(imagesPath+name+".jpg"))
        scene.setSceneRect(QtCore.QRectF(0,0,2,2))
        select_character_window.graphicsView.setScene(scene)
        """
        #find a better way for the picture!
        pixmap = QtGui.QPixmap(imagesPath+name+".jpg")
        select_character_window.picture_label.setPixmap(pixmap)#QtGui.QPixmap(imagesPath+name+".jpg"))

    def nextStep_event(self):
        print(order[self.orderSelect])

        if (order[self.orderSelect]=='complete'):
            self.orderSelect = 0

        elif(order[self.orderSelect]=='PAO1'):
            self.orderSelect+=1
            self.setupCharacterWindow()
            #MainWindow.close()
            characterWindow.show()
        elif(order[self.orderSelect]=='PAO2'):
            self.orderSelect += 1
            self.setupCharacterWindow()
            #MainWindow.close()
            characterWindow.show()
        elif(order[self.orderSelect]=='Number'):
            self.orderSelect += 1
        else:
            self.orderSelect+=1


    def confirmPasswordCreated_event(self):
        loginWindow.show()

if __name__ == "__main__":
    myApp = passwordGenerator()
    myApp.openWindow()