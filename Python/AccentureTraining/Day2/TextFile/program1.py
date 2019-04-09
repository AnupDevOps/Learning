#ReadWrite Text files
path = r"C:\Users\anup.b.kumar.mishra\Desktop\Learning\python\AccentureTraining\Day2\TextFile"
fileobj=open("data.txt", 'r')
print(fileobj)
#print(fileobj.read())
#print(fileobj.readlines())

mylist = fileobj.readlines()
for val in mylist:
    print(val)
fileobj.seek(0) #rewinding the file means setting the file on first line of file

print(fileobj.readlines(1))
print(fileobj.readlines(2))

fileobj.close()

fileobj = open("test1.txt",'w')
str =  'welcome to accenture'
fileobj.write(str)

mylist = ['this','is','a','sample','file']
fileobj.writelines(mylist)

print("Whether writable ?: ", fileobj.writable())
print("Whether seekable ?: ", fileobj.seekable())
print("Whether readable ?: ", fileobj.readable())
print("Whether mode ?: ", fileobj.mode)

fileobj.close()

