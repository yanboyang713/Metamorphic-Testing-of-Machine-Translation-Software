from openpyxl import Workbook
workbook = Workbook()
workSheetOne = workbook.active
workSheetOne.title = "Chinese"
workSheetTwo = workbook.create_sheet("Swedish")
workSheetThree = workbook.copy_worksheet (workSheetOne)
workSheetThree.title = "Japanese"

for sheet in workbook:
    print (sheet.title)

for i in range(0, 10):
    workSheetOne['A' + str(i + 1)] = "hello word"
workbook.save("csci318.xlsx")
