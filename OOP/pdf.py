print("======================== PDF Merger ========================")
import os
from PyPDF2 import PdfWriter


merger = PdfWriter()
os.chdir("OOP/pdfMerger")
files = os.listdir()


for pdfs in files:
    if pdfs.endswith(".pdf"):
        print(pdfs)
        merger.append(pdfs)

merger.write("compositePDFFile.pdf")

merger.close()
