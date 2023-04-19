#!/usr/bin/python3

import xlwt
from xlwt import Workbook
workBook=Workbook()
workSheet=workBook.add_sheet("Sheet no 1")

style=xlwt.easyxf('font: bold 1, underline 1;')

workSheet.write(0,0,'SERIAL',style)
workSheet.write(0,1,'NAMES',style)

workSheet.write(1,0,'A-No-1')
workSheet.write(2,0,'B-No-2')
workSheet.write(3,0,'C-No-3')
workSheet.write(4,0,'D-No-4')
workSheet.write(5,0,'E-No-5')
workSheet.write(6,0,'F-No-6')
workSheet.write(1,1,'ABHI')
workSheet.write(2,1,'JAMES')
workSheet.write(3,1,'ANGEL')
workSheet.write(4,1,'ARUN')
workSheet.write(5,1,'ALICE')
workSheet.write(6,1,'HENRY')

workBook.save('veri_yaz.xls')
print("\n---Kayit Basarili---\n")

