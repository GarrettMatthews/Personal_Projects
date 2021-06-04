from openpyxl import load_workbook
import os
import csv

if os.path.exists("./Clean/pnl.csv"):
    os.remove("./Clean/pnl.csv")

sheet_list = ["P&L Summary"]
file_lyst = []
path = "../../Dropbox/VRT Reporting/2021 DAILY REPORT/2021.06/"

for file in os.listdir(path):
    filename = os.fsdecode(file)
    if filename.endswith(".xlsx"):
        fyle = path + filename
        file_lyst.append(fyle)


# Sheet needed: P&L Summary
for i in file_lyst:
    if "TIME" in i or "Time" in i:
        continue
    print("Loading: > " + i)
    data = load_workbook(i, data_only=True)
    for r in sheet_list:
        lyst = []
        sheet = data[r]
        row = list(sheet.rows)
        for j in row:
            temp = []
            for k in j:
                temp.append(k.value)
            lyst.append(temp)
        fylname = "./Clean/pnl.csv"
        if os.path.isfile(fylname):
            lyst = lyst[1:]
        file = open(fylname, 'a', newline = '')
        with file:
            write = csv.writer(file)
            write.writerows(lyst)
        print(i, " successfully copied over \n")

