Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3+2
5
>>> _
5
>>> _*3
15
>>> _*10
150
>>> print("World is here")
World is here
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> type(10)
<class 'int'>
>>> type("hello")
<class 'str'>
>>> type("a")
<class 'str'>
>>> type("10")
<class 'str'>
>>> type(100.3)
<class 'float'>
>>> mystr="accenture is here"
>>> mystr
'accenture is here'
>>> print(mystr)
accenture is here
>>> mystr=10
>>> mystr
10
>>> type(mystr)
<class 'int'>
>>> mystr=M
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    mystr=M
NameError: name 'M' is not defined
>>> mystr="M"
>>> Mystr
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Mystr
NameError: name 'Mystr' is not defined
>>> 59/60
0.9833333333333333
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> 

>>> "15" + 2
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    "15" + 2
TypeError: can only concatenate str (not "int") to str
>>> org_name="accenture"
>>> location="Hydrabad"
>>> print(org_name+location)
accentureHydrabad
>>> "15" *3
'151515'
>>> "Accenture" *3
'AccentureAccentureAccenture'
>>> str=input()
anup
>>> print(str)
anup
>>> str1="All"
>>> str2="work"
>>> str3="and"
>>> str4="no"
>>> str5="play"
>>> str1+str2+str3+str4+str5
'Allworkandnoplay'
>>> str1+" "+str2+str3+str4+str5
'All workandnoplay'
>>> str1+" "+str2+" "+str3+" "+str4+" "+str5
'All work and no play'
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> 10 == 10
True
>>> 10 == 9
False
>>> a = 100
>>> if a== 100:
	print("value of a is 100")
print("good bye")
SyntaxError: invalid syntax
>>> int(1.0)
1
>>> int(2.33333)
2
>>> float(1)
1.0
>>> int("hello")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
>>> True or False
True
>>> True and False
False
>>> True or 7
True
>>> "happy" and "sad"
'sad'
>>> "happy" or "sad"
'happy'
>>> 
>>> "" and "sad"
''
>>> "happy" or ""
'happy'
>>> "happy" and ""
''
>>> n=234
>>> len(n)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    len(n)
TypeError: object of type 'int' has no len()
>>> len(n)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    len(n)
TypeError: object of type 'int' has no len()
>>> 
