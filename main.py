import PyPDF2 as pypdf
from PyPDF2 import PdfFileWriter

pwrite = PdfFileWriter()


def findInDict (needle, haystack):
    for key in haystack.keys():
        try:
            value = haystack[key]
        except:
            continue
        if key == needle:
            return value
        if isinstance(value,dict):
            x =findInDict(needle, value)
            if x is not None:
                return x


pdfobject = open('./Data/Shortened1/Doc0.pdf', 'rb')

pdf = pypdf.PdfFileReader(pdfobject)

print(pdf.getDocumentInfo())