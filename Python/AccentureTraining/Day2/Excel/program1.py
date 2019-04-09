# working with CSV 
import csv
filehandle = open('sheet.csv')
print(filehandle)
readobj = csv.reader(filehandle)
dataobj =  list(readobj)

print(dataobj)

for row in dataobj:
    print(str(row))

filehandle.close()

#Writecsv.py

import csv
outputfile=open('output.csv','w',newline='')
outputWriter=csv.writer(outputfile)
outputWriter.writerow(['123','John','5000'])
outputWriter.writerow(['124','Jenny','6000'])
outputWriter.writerow(['125','Jack','7000'])
outputWriter.writerow(['126','Joseph','8000'])
outputWriter.writerow(['127','Mary','5000'])
outputWriter.writerow(['128','Johnny','9000'])
outputfile.close()
print("Data written in output.csv")

##pip install openpyxl --installing pip 
##python -m pip install --user openpyxl
##Shell- import openpyxl 
