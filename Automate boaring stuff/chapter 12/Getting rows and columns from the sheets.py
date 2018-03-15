import openpyxl
wb=openpyxl.load_workbook('CONCRETE QTY FOR ABUTMENTS.xlsx')
sheet = wb.get_sheet_names('5.295')
print(tuple(sheet['A1':'C3']))
for rowofcellobjects in sheet['A1':'C3']:
     for cellobj in  rowofcellobjects:
        print(cellobj.coordinate,cellobj.value)
     print('----END OF ROW----')