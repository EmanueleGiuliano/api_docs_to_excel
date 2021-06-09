import os
import sys
import re
import ast 
from os import listdir
from os.path import isfile, join
import json
import xlsxwriter

input_path = sys.argv[1]
env = sys.argv[2]
u_service = sys.argv[3]
filename = sys.argv[4]

print("processing file: " + input_path)

workbook = xlsxwriter.Workbook(filename + '.xlsx')
worksheet = workbook.add_worksheet()

intestazione_format = workbook.add_format()
intestazione_format.set_bold()
intestazione_format.set_font_color('white')
intestazione_format.set_bg_color('blue')

worksheet.write(0, 0, 'AMBIENTE', intestazione_format)
worksheet.write(0, 1, 'HOST', intestazione_format)
worksheet.write(0, 2, 'API'     , intestazione_format)
worksheet.write(0, 3, 'TIPO REST' , intestazione_format)
worksheet.write(0, 4, 'NOME MICROSERVZIO', intestazione_format)
worksheet.write(0, 5, 'NOTE', intestazione_format)
worksheet.write(0, 6,  'DERIVAZIONE/FALLBACK', intestazione_format)
worksheet.write(0, 7,  'CENSIM.WSRR', intestazione_format)
worksheet.write(0, 8,  'URL DATAPOWER WSSR', intestazione_format)
worksheet.write(0, 9,  'SWAGGER', intestazione_format)

row = 1

with open(input_path) as f:
  data = json.load(f)

print(data['host'])
print(data['basePath'])

swagger_url = data['host']+"/swagger-ui.html"

for path in data['paths']:
    print(path)
    for method in data['paths'][path]:
        worksheet.write(row, 0,  env)
        worksheet.write(row, 1,  data['host'])
        worksheet.write(row, 2,  path)
        worksheet.write(row, 3,  method)
        worksheet.write(row, 4,  u_service)
        worksheet.write(row, 9,  swagger_url)
        
        print(method + "\n")
        row= row+1

workbook.close()