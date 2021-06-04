from openpyxl import load_workbook
import os

ym = input("What is the year.month combination for the file? > ")

wb = load_workbook("./Master_Template.xlsx")

plant_lyst = ["CC1", "CC2", "Alek Time", "DA4", "HMA2 Cone", "HMA2 Pre-Screen", "HMA2 Sand Plant", "HMA2 VSI",
              "Hoff Time", "PC2", "RLO", "Skyler Time", "Special Projects"]

for i in plant_lyst:
    file_name = ym + " " + i + ".xlsx"
    wb.save(filename= file_name)
    print(i + " completed")


