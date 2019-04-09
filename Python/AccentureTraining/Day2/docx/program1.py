# Install python-docx
#ReadDoc.py

import docx

doc = docx.Document('demo.docx')

print(len(doc.paragraphs))

print(doc.paragraphs[0].text)
print(doc.paragraphs[1].text)
print(doc.paragraphs[2].text)
print(doc.paragraphs[3].text)
print(doc.paragraphs[4].text)
print(doc.paragraphs[5].text)
print(doc.paragraphs[6].text)


print("writing with for loop")
lenght=int(len(doc.paragraphs))
for l in range(1,lenght-1):
    print(doc.paragraphs[l].text)


doc=docx.Document()

doc.add_paragraph("welcome")
doc.add_paragraph("welcome2")
doc.add_paragraph("welcome3")

doc.save("helloworl.docx")
print("DOne")
