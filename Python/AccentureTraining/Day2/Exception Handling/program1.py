# Exception handling

#print(1/0)
x = {1:2,2:3}
#print(x[3])

#print(b)

try:
    print(1/0)
#    print(b)
except ZeroDivisionError as e:
    print(e)



try:
#    print(1/0)
    print(b)
except NameError as e:
    print(e)


try:
    print(b)
except KeyError as e:
    print(e)
except IndexError as e:
    print(e)
except:
    print("Unknown Error")
finally:
    print("Oh Bug Kal ana")
