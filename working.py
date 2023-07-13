from openpyxl import Workbook , load_workbook

wb = Workbook()
ws = wb.active
ws.title = "Data"

# append rows

ws.append(['Bambo' , 'Is' , 'A' , 'Great' , 'Guy' , '!'])
ws.append(['Bambo' , 'Is' , 'A' , 'Great' , 'Guy' , '!'])
ws.append(['Bambo' , 'Is' , 'A' , 'Great' , 'Guy' , '!'])
ws.append(['end'])

wb.save('bambo.xlsx')