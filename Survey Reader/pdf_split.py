import PyPDF2 as pypdf
import os


def main():
    file_lyst = []
    name_lyst = []
    for file in os.listdir("./Data/Completed/"):
        filename = os.fsdecode(file)
        if filename.endswith(".pdf"):
            fyle = "./Data/Completed/" + filename
            file_lyst.append(fyle)
            name_lyst.append(filename)
    for i in file_lyst:
        inputPDF = pypdf.PdfFileReader(open(i, "rb"))

        for j in range(inputPDF.numPages):
            output = pypdf.PdfFileWriter()
            output.addPage(inputPDF.getPage(j))
            new_file = "./Split/" + name_lyst[file_lyst.index(i)] + "-page%s.pdf" % j
            with open(new_file, "wb") as outputStream:
                output.write(outputStream)
            print("Page " + str(j) + " of " + i + " split and saved \n")
        print(i + " finished being split \n")


if __name__ == '__main__':
    main()
