#!/usr/bin/python3

import xlrd

filePath = "/home/pi/veri/veri_yaz.xls"
openFile = xlrd.open_workbook(filePath)

sheet = openFile.sheet_by_name("Sheet No 1")

print("\nNumber of Rows : ",sheet.nrows)
print("\nNumber of Columns : ",sheet.ncols)
print("\nColumn Names : ", end=' ')

for i in range(sheet.ncols): 
 print(sheet.cell_value(0, i), end=', ')

print("\n\nFirst-Column  Second-Column")

for i in range(sheet.nrows):
 print(sheet.cell_value(i,0), " ", sheet.cell_value(i,1))
