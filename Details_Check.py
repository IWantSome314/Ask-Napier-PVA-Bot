#!/usr/bin/env python 3

import openpyxl
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

wb = load_workbook("Tenants_Details.xlsx")

ws = wb.active
NamesList = []
for row in ws:
    name = row[2].value
    NamesList.append(name)
 
UserName = input("Please enter your details: ")
if UserName in NamesList:
    print("Verfied")
else:
    print("Well shit")+ quit()