from myExcel import myExcel

xlsheet = myExcel()#"A:\Desktop\myProject\Project Files\Words.xlsx");

name = xlsheet.getRandomItem("Object",'C')
print("\nthe name is", name)