from myExcel import myExcel

xlsheet = myExcel()#"A:\Desktop\myProject\Project Files\Words.xlsx");

name = xlsheet.getRandomItem("Object",'C')
print("\nthe name is", name)
print();
for number in range(1,26):
    print(xlsheet.getRandomName(number))
