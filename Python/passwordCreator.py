import sys
import re
import random
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import QObject

from myExcel import myExcel
sys.path.append("A:/Desktop/myProject/Python/UI forms")

from backgroundWindow import Ui_BackgroundWindow
from beforeStarting import Ui_beforeStarting
from calculateNumbers import Ui_calculateNumbersWindow
from createUserWindow import Ui_createUserWindow
from forgotPassword import Ui_forgotPasswordWindow
from KeyPad import Ui_keyPad
from learningPassword import Ui_learningPasswordWindow
from loginWindow import Ui_loginWindow
from mainWindow import Ui_MainWindow
from myDialog import Ui_myDialog
from numberWindow import Ui_numberWindow
from PAO2selectCharacterWindow import Ui_PAO2characterWindow
from routineCheck import Ui_Dialog
from selectCharacterWindow import Ui_characterWindow
from selectCharacterWindow2 import Ui_characterSentenceWindow2
from selectSymbolWindow import Ui_selectSymbol
from createUserWindow import Ui_createUserWindow
from myUser import createUser

xlsheet = myExcel()
imagesPath = "A:/Desktop/myProject/Project Files/Images/"
symbolsPath = "A:/Desktop/myProject/Project Files/Symbols/"
buttonName = ""

myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
order_normal_mode = ['PAO1', 'Number', 'Symbol']
order_medium_mode = ['PAO1', 'PAO2', 'Number', 'Symbol']

app = QtGui.QApplication(sys.argv)
#MainWindow = QtGui.QMainWindow()
#loginWindow = QtGui.QWidget()
#createUserWindow = QtGui.QWidget()
#characterWindow = QtGui.QWidget()
#numberWindow = QtGui.QWidget()
#symbolWindow = QtGui.QWidget()

backgroundWindow = QtGui.QWidget()
beforeStarting = QtGui.QWidget()
calculateNumbers = QtGui.QWidget()
createUserWindow = QtGui.QWidget()
forgotPassword = QtGui.QWidget()
KeyPad = QtGui.QWidget()
learningPassword = QtGui.QWidget()
loginWindow = QtGui.QWidget()
mainWindow = QtGui.QWidget()
myDialog = QtGui.QWidget()
numberWindow = QtGui.QWidget()
PAO2selectCharacterWindow =QtGui.QWidget()
routineCheck = QtGui.QWidget()
selectCharacterWindow = QtGui.QWidget()
selectCharacterWindow2 = QtGui.QWidget()
selectSymbolWindow = QtGui.QWidget()
createUserWindow = QtGui.QMainWindow()

"""
main_window = Ui_MainWindow()
create_user_window = Ui_createUserWindow()
login_window = Ui_loginWindow()
select_character_window = Ui_characterWindow()
select_character_window_2 =Ui_characterWindow()
number_window = Ui_numberWindow()
symbol_window = Ui_selectSymbol()
"""

background_window = Ui_BackgroundWindow()
before_starting_window = Ui_beforeStarting()
calculate_numbers = Ui_calculateNumbersWindow()
create_user_window = Ui_createUserWindow()
forgot_password = Ui_forgotPasswordWindow()
keypad_window = Ui_keyPad()
# learningPassword = Ui_form()
login_window = Ui_loginWindow()
main_window = Ui_MainWindow()
my_dialog = Ui_myDialog()
number_window = Ui_numberWindow()
PAO2_select_character_window = Ui_PAO2characterWindow()
routine_check = Ui_Dialog()
select_character_window = Ui_characterWindow()
select_character_window_2 = Ui_characterSentenceWindow2()
select_symbol_window = Ui_selectSymbol()

class passwordGenerator(QtGui.QWidget):
    orderSelect = 0
    current_user = createUser()
    myOrder = ""
    dialogAttempts = 0
    def __init__(self):
        super(passwordGenerator, self).__init__()

        """
        main_window.setupUi(MainWindow)
        create_user_window.setupUi(createUserWindow)
        login_window.setupUi(loginWindow)
        select_character_window.setupUi(characterWindow)
        number_window.setupUi(numberWindow)
        symbol_window.setupUi(symbolWindow)
        """

        #background_window.setupUi(backgroundWindow)
        before_starting_window.setupUi(beforeStarting)
        calculate_numbers.setupUi(calculateNumbers)
        create_user_window.setupUi(createUserWindow)
        forgot_password.setupUi(forgotPassword)
        keypad_window.setupUi(KeyPad)
        # learningPassword.setupUi(learningPassword)
        login_window.setupUi(loginWindow)
        main_window.setupUi(mainWindow)
        my_dialog.setupUi(myDialog)
        number_window.setupUi(numberWindow)
        PAO2_select_character_window.setupUi(PAO2selectCharacterWindow)
        routine_check.setupUi(routineCheck)
        select_character_window.setupUi(selectCharacterWindow)
        select_character_window_2.setupUi(selectCharacterWindow2)
        select_symbol_window.setupUi(selectSymbolWindow)
        create_user_window.setupUi(createUserWindow)
        my_dialog.buttonBox.clicked.connect(self.dialogClose)
        select_symbol_window.pushButton_2.clicked.connect(self.setupSymbolWindow)

    def openWindow(self):
        random.shuffle(order_normal_mode)
        random.shuffle(order_medium_mode)
        order_normal_mode.insert(len(order_normal_mode), 'complete')
        order_medium_mode.insert(len(order_medium_mode), 'complete')
        before_starting_window.pushButton.clicked.connect(self.closeInfo)
        main_window.createNewPassword_btn.clicked.connect(self.nextStep_event) #Normal
        main_window.createNewPassword_btn_2.clicked.connect(self.nextStep_event)  # Normal
        #main_window.createNewPassword_btn_2.connect(self.nextStep_event)  #Medium
        #main_window.confirmPasswordCreated_btn.connect(self.confirmPasswordCreated_event)  # Check password
        self.current_user = createUser()
        self.setupCharacterWindow(select_character_window)
        self.setupCharacterWindow(PAO2_select_character_window)
        #self.setupCharacterWindow(select_character_window_2)
        main_window.createNewPassword_btn.setObjectName("Normal Passwords")
        main_window.createNewPassword_btn_2.setObjectName("Medium Passwords")
        #createUserWindow.show()
        #loginWindow.show()
        mainWindow.show()
        beforeStarting.show()
        sys.exit(app.exec_())

    def closeInfo(self):
        beforeStarting.close()

    def setupCharacterWindow(self, charWindow):
        random.shuffle(myList)
        self.setupCW(charWindow.btn_1, myList[1])
        self.setupCW(charWindow.btn_2, myList[2])
        self.setupCW(charWindow.btn_3, myList[3])
        self.setupCW(charWindow.btn_4, myList[4])
        self.setupCW(charWindow.btn_5, myList[5])
        self.setupCW(charWindow.btn_6, myList[6])
        self.setupCW(charWindow.btn_7, myList[7])
        self.setupCW(charWindow.btn_8, myList[8])
        self.setupCW(charWindow.btn_9, myList[9])
        self.setupCW(charWindow.btn_10, myList[10])
        self.setupCW(charWindow.btn_11, myList[11])
        self.setupCW(charWindow.btn_12, myList[12])
        self.setupCW(charWindow.btn_13, myList[13])
        self.setupCW(charWindow.btn_14, myList[14])
        self.setupCW(charWindow.btn_15, myList[15])
        self.setupCW(charWindow.btn_16, myList[16])
        self.setupCW(charWindow.btn_17, myList[17])
        self.setupCW(charWindow.btn_18, myList[18])
        self.setupCW(charWindow.btn_19, myList[19])
        self.setupCW(charWindow.btn_20, myList[20])
        self.setupCW(charWindow.btn_21, myList[21])
        self.setupCW(charWindow.btn_22, myList[22])
        self.setupCW(charWindow.btn_23, myList[23])
        self.setupCW(charWindow.btn_24, myList[24])
        self.setupCW(charWindow.btn_25, myList[25])
        self.setupCW(charWindow.btn_26, myList[0])

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
        
        #find a better way for the picture!
        pixmap = QtGui.QPixmap(imagesPath+name+".jpg")
        select_character_window.picture_label.setPixmap(pixmap)#QtGui.QPixmap(imagesPath+name+".jpg"))
        """
        myIconSize = QtCore.QSize(151, 151)
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(imagesPath + name + ".jpg"))
        select_character_window.pushButton.setIcon(myIcon)
        select_character_window.pushButton.setIconSize(myIconSize)

    def closeWindows(self):
        myDialog.close()
        calculateNumbers.close()
        createUserWindow.close()
        forgotPassword.close()
        KeyPad.close()
        learningPassword.close()
        loginWindow.close()
        mainWindow.close()
        numberWindow.close()
        routineCheck.close()
        selectCharacterWindow.close()
        #selectCharacterWindow2.close()
        selectSymbolWindow.close()
        createUserWindow.close()

    def nextStep_event(self):
        self.closeWindows()
        pushedBy = self.sender().objectName()
        print("puched by {}".format(pushedBy))
        if (pushedBy != "Normal Passwords" and pushedBy != "Normal Passwords"):
            routine_check.ok_btn.clicked.connect(self.checkiftestispassed)
            routine_check.ok_btn.setObjectName(pushedBy)
            routineCheck.show()
        else:
            self.testPassed()

    def checkiftestispassed(self):
        pushedBy = self.sender().objectName()

        if(routine_check.passwordCheck_le.text()== self.current_user.password):
            self.dialogAttempts = 0
        else:
            self.dialogAttempts = self.dialogAttempts+1
            dialogString = "That is not the current password! Include all the passwords up to this point\n you have a total of " + str(4-self.dialogAttempts)+ " attempts left."
            my_dialog.label.setText(dialogString)
            myDialog.show()

        if(self.dialogAttempts == 0):
            routineCheck.close()
            self.testPassed()
        elif(self.dialogAttempts == 4):
            dialogString= "The password that we have on file is '"+ self.current_user.password+ "' remember it for next time."
            my_dialog.label.setText(dialogString)
            myDialog.show()
            self.dialogAttempts = 0
            self.testPassed()

    def testPassed(self):
        self.closeWindows()

        pushedBy = self.sender().objectName()

        if (pushedBy == "Normal Passwords"):
            self.myOrder = order_normal_mode
        elif (pushedBy == "Medium Passwords"):
            self.myOrder = order_medium_mode

        print(self.myOrder[self.orderSelect])

        if (self.myOrder[self.orderSelect]=='complete'):
            self.orderSelect = 0

        elif(self.myOrder[self.orderSelect]=='PAO1'):
            self.orderSelect+=1
            #MainWindow.close()
            select_character_window.next_btn.setObjectName("PAO1")
            select_character_window.next_btn.clicked.connect(self.characterSelected)
            selectCharacterWindow.show()
        elif(self.myOrder[self.orderSelect]=='PAO2'):
            self.orderSelect += 1
            PAO2_select_character_window.next_btn.setObjectName("PAO2")
            PAO2_select_character_window.next_btn.clicked.connect(self.characterSelected)
            #MainWindow.close()
            selectCharacterWindow.show()
        elif(self.myOrder[self.orderSelect]=='Number'):
            self.orderSelect += 1
            xlsheet.getRandomNumber(self.current_user)
            myString = ("Your numbers are " + str(self.current_user.number_1)+ " and " +str(self.current_user.number_2)+ " you will need to " +str(self.current_user.operation)+" them.")
            calculate_numbers.label_2.setText(myString)
            calculateNumbers.show()
        else:
            self.orderSelect+=1
            select_symbol_window.next_btn.clicked.connect(self.saveSymbol)
            selectSymbolWindow.show()

    def confirmPasswordCreated_event(self):
        loginWindow.show()

    def setupSymbolWindow(self):
        mySymbol = xlsheet.getRandomSymbol()
        myIconSize = QtCore.QSize(101, 101)
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(symbolsPath + mySymbol + ".jpg"))
        select_symbol_window.image.setIcon(myIcon)
        select_symbol_window.image.setIconSize(myIconSize)
        select_symbol_window.symbolName_label.setText(mySymbol)
        select_symbol_window.label_4.setText(xlsheet.suggestion)
        print(mySymbol)

    def saveSymbol(self):
        if(select_symbol_window.lineEdit.text()!=""):
            symbolString = select_symbol_window.lineEdit.text()
            self.current_user.symbol = symbolString
            self.current_user.addToPassword(symbolString)
            self.nextStep_event()

    def dialogClose(self):
        myDialog.close()

    def characterSelected(self):
        pushedBy = pushedBy = self.sender().objectName()
        print("character selected")
        nameR = select_character_window.password_label.text()
        myName = select_character_window.name_label.text()
        myAction = xlsheet.getRandomItem("Action")
        myObject = xlsheet.getRandomItem("Object")
        myIconSize = QtCore.QSize(81, 81)

        #select_character_window_2.name_label.setText(myName)
        select_character_window_2.action_label.setText(myAction)
        select_character_window_2.object_label.setText(myObject)
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(imagesPath + myName + ".jpg"))
        select_character_window_2.pushButton.setIcon(myIcon)
        select_character_window_2.pushButton.setIconSize(myIconSize)
        select_character_window_2.pushButton.setToolTip(myName)
        psswString = nameR + myAction[0]+myObject[0]

        if(pushedBy== "PAO1"):
            print("PAO1")
            self.current_user.PAO1_person = myName
            self.current_user.PAO1_object = myObject
            self.current_user.PAO1_action = myAction
            self.current_user.PAO1_full = psswString
            selectCharacterWindow.close()
        elif (pushedBy == "PAO2"):
            print("PAO2")
            self.current_user.PAO2_person = myName
            self.current_user.PAO2_object = myObject
            self.current_user.PAO2_action = myAction
            self.current_user.PAO2_full = psswString
            PAO2selectCharacterWindow.close()
        self.current_user.addToPassword(psswString)

        selectCharacterWindow2.show()


if __name__ == "__main__":
    myApp = passwordGenerator()
    myApp.openWindow()