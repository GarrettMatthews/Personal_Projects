import PyPDF2 as pypdf
from PyPDF2 import PdfFileWriter
import os


def start(lyst):
    kind = input("Do you want to open Version 1 or Version 2 - enter an integer")
    folder = "Version"+kind
    basepath = "./Data/"+folder
    for i in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, i)):
            lyst.append(i)
    return basepath


def pdf_edit(doc_count, og_file, folder_structure):
    pdf_in = open(folder_structure+"/"+og_file, "rb")
    pdf = pypdf.PdfFileReader(pdf_in)
    page = pdf.getPage(3)
    pwrite = PdfFileWriter()
    pwrite.addPage(page)
    with open("./Data/Shortened2/Doc"+str(doc_count)+".pdf", "wb") as out_file:
        pwrite.write(out_file)


def main():
    file_lyst = []
    folder = start(file_lyst)
    x = 0
    for i in range(len(file_lyst)):
        pdf_edit(x, file_lyst[x], folder)
        x += 1
    print("Job completed")


if __name__ == '__main__':
    main()