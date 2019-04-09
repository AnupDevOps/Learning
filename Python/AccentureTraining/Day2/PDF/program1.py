#Insatll PyPDF2


#ReadPDF.py

import PyPDF2

pdfobj = open('acn.pdf', 'rb')

readerobj = PyPDF2.PdfFileReader(pdfobj)
print(readerobj)

print(readerobj.numPages)

pagedata = readerobj.getPage(0)
data = pagedata.extractText()
print(data)


#TO DO
print("........................ Using For Loop.......................")

# Print all data
for con in range(1,(readerobj.numPages-1)):
    pagedata = readerobj.getPage(con)
    data = pagedata.extractText()
    print(data)
