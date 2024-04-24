import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

with open('resource/exams.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        ws.append(row)

wb.save('resource/excel-data.xlsx')
