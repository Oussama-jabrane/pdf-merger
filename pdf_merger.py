from PyPDF2 import PdfMerger
from sys import argv

merger = PdfMerger()

input1 = argv[1]
input2 = argv[2]

file1 = open(input1, "rb")
file2 = open(input2, "rb")

merger.append(file1)
merger.append(file2)

output = open("merged-pdf.pdf", "wb")
merger.write(output)