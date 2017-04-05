import xlrd
import random

class myExcel(object):
    #filepath = ""

    #def __init__(self):
        #self.filepath = filepath

    #print(filepath)
    filepath = "A:\Desktop\myProject\Project Files\Words.xlsx"

    workbook = xlrd.open_workbook(filepath)
    sheet_names = workbook.sheet_names()
    sheet0 = workbook.sheet_by_name(sheet_names[0])

    row = sheet0.row(0)
    from xlrd.sheet import ctype_text

    def getRandomItem(self, itemType, letter):

        while True:
            randomNumber = random.randint(0,100)
            #print(randomNumber)

            try:
                #name = xlsheet.getName(5, 'E')
                counter = 0
                rowIndex = self.getRow(letter)
                # print("letter row: ", letter, rowIndex)
                for idx, cell in enumerate(self.row):
                    # cell_type_str = ctype_text.get(cell.ctype, 'unknown type')
                    if (cell.value.startswith(itemType)):
                        counter = counter + 1

                randomNumber = randomNumber % counter
                for idx, cell in enumerate(self.row):
                    if (cell.value.startswith(itemType)):
                        if (randomNumber == 0):
                            # this is the column
                            name = self.sheet0.cell(rowIndex, idx)
                            #print(name)
                            break
                        else:
                            randomNumber = randomNumber - 1
            except:
                print();

            if name=="":
                print("trying again")
            else:
                break;


        return name

    def getRow(self, character):
        return{
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










