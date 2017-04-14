import sys
import xlrd
import random
from myUser import createUser

# from xlrd.sheet import ctype_text

class myExcel(object):
    # filepath = ""

    # def __init__(self):
    # self.filepath = filepath
    maxCharacters = 47
    # print(filepath)
    filepath = "A:\Desktop\myProject\Project Files\Words.xlsx"

    workbook = xlrd.open_workbook(filepath)
    sheet_names = workbook.sheet_names()
    sheet0 = workbook.sheet_by_name(sheet_names[0])
    row = sheet0.row(0)
    suggestion = ""

    def getRandomItem(self, itemType, letter):

        while True:
            # print(randomNumber)

            try:
                # name = xlsheet.getName(5, 'E')
                counter = 0
                rowIndex = self.getRow(letter)
                # print("letter row: ", letter, rowIndex)
                for idx, cell in enumerate(self.row):
                    # Counting the columns in that type of item
                    if (cell.value.startswith(itemType)):
                        counter = counter + 1

                randomNumber = random.randint(0, counter*7)
                randomNumber = randomNumber % counter
                for idx, cell in enumerate(self.row):
                    if (cell.value.startswith(itemType)):
                        if (randomNumber == 0):
                            # this is the column
                            info = str(self.sheet0.cell(rowIndex, idx))
                            #print(info)
                            break
                        else:
                            randomNumber = randomNumber - 1

                if info =="text:''":
                    print("trying again")
                else:
                    name = info[6:len(info)-1]#+info[:len(info)-1]
                    #print(info)
                    #print (name)
                    break

            except Exception:
                print("Unexpected error: ",e = sys.exc_info()[0]);

        return name

    def getRandomSymbol(self):
        #Character Icon
        randomNumber = random.randint(2, self.maxCharacters)
        for idx, cell in enumerate(self.row):
            if (cell.value.startswith("Character Icon")):
                #print(randomNumber, idx)
                myCol = idx

        info = str(self.sheet0.cell(randomNumber, myCol))
        name = info[6:len(info) - 1]  # +info[:len(info)-1]
        mySug = str(self.sheet0.cell(randomNumber, (myCol - 2)))  # The characters are 2 columns to the left
        #mySug = mySug[6:len(info) - 1]
        #mySug = mySug[len(info)]
        #self.suggestion = mySug
        self.suggestion= mySug[6:(len(info) - 1):]
        print(self.suggestion)

        return name

    def getRandomName(self, rowIndex):

        while True:
            randomNumber = random.randint(0,40)
            #print(randomNumber)

            try:
                # name = xlsheet.getName(5, 'E')
                counter = 0
                # print("letter row: ", letter, rowIndex)
                for idx, cell in enumerate(self.row):
                    # Counting the columns in that type of item
                    if (cell.value.startswith("Name")):
                        counter = counter + 1

                randomNumber = randomNumber % counter
                for idx, cell in enumerate(self.row):
                    if (cell.value.startswith("Name")):
                        if (randomNumber == 0):
                            # this is the column
                            info = str(self.sheet0.cell(rowIndex, idx))
                            #print(info)
                            break
                        else:
                            randomNumber = randomNumber - 1

                if (str(info) != "text:''" and str(info) != "empty:''"):
                    #print(info)
                    name = info[6:len(info)-1]#+info[:len(info)-1]
                    #print(info)
                    #print (name)
                    break

            except Exception:
                print("Unexpected error: ",e = sys.exc_info()[0]);

        return name

    def getRandomNumber(self, user):
        flag = True;

        while(flag):
            operation = random.randint(1,4)

            if (operation == 1):        #Sum
                print("sum")
                user.operation = "add"
                number1 = random.randint(0,9)
                number2 = random.randint(0,9)
                result = number1 +number2
                flag = False;
            elif(operation == 2):       #Rest
                print("r")
                user.operation = "substract"
                number1 = random.randint(0, 9)
                number2 = random.randint(0, 9)
                result = number1 - number2
                flag = False;
            elif(operation==3):         #Mult
                print("m")
                user.operation = "multiply"
                number1 = random.randint(0, 9)
                number2 = random.randint(0, 9)
                result = number1 * number2
                flag = False;
            elif(operation == 4):
                print("d")
                user.operation = "divide"
                while(True):
                    number1 = random.randint(0, 9)
                    number2 = random.randint(0, 9)

                    try:
                        result = number1 / number2
                    except:
                        result = 1

                    if((result ==0) and (number1>number2)):
                        continue;
                flag = False;
            else:
                user.operation = "exponentiation"

        user.number_1 = number1
        user.number_2 = number2
        user.number_result = result
        fullnumber =str(number1)+str(number2)+str(result)
        user.number_full = fullnumber
        user.addToPassword(fullnumber)


    def getRow(self, character):
        return {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26,
        }[character]


if __name__== "__main__":
    user = createUser()
    aj = myExcel()
    aj.getRandomNumber(user)
    print("Number 1: {}\nNumber 2: {}\nOperation: {}\nResult: {}".format(user.number_1, user.number_2, user.operation, user.number_result))




