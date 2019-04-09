import sqlite3

conn = sqlite3.connect('student.db')
#conn.execute('create table STUDENT(ID INT PRIMARY KEY, NAME CHAR(10),MARKS REAL)')

try:
    conn.execute("INSERT INTO STUDENT(ID,NAME,MARKS) VALUES(121,'Vijay',95.5)")
    conn.execute("INSERT INTO STUDENT(ID,NAME,MARKS) VALUES(132,'Murali',98.5)")
    conn.execute("INSERT INTO STUDENT(ID,NAME,MARKS) VALUES(1,'RAMAN',99.5)")
    conn.execute("INSERT INTO STUDENT(ID,NAME,MARKS) VALUES(10,'Sandu',90.5)")
    conn.execute("INSERT INTO STUDENT(ID,NAME,MARKS) VALUES(11,'Raju',91.5)")
    conn.execute("INSERT INTO STUDENT(ID,NAME,MARKS) VALUES(12,'HI',61.5)")
except sqlite3.IntergrityError as e:
    print(e)

# Print DB DATA

#print(conn.execute("SELECT * FROM STUDENT"))

cur = conn.execute('SELECT ID, NAME, MARKS FROM STUDENT')

for val in cur:
    print(val)

print("....................... print data in list ...........................")
cur = conn.execute('SELECT * FROM STUDENT')
b = list(cur)
print(b)

# Delete DB DATA
print("....................... Delete DB DATA ...........................")
cur =conn.execute('DELETE FROM STUDENT WHERE MARKS < 70')
cur = conn.execute('SELECT ID, NAME, MARKS FROM STUDENT')

for val in cur:
    print(val)


#conn.commit() # it help us get old data in database as well.


conn.execute("UPDATE student SET marks=100 where id=103")
cur = conn.execute('SELECT ID, NAME, MARKS FROM STUDENT')

for val in cur:
    print(val)

conn.close()
