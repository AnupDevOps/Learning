print("Dictionary")
nameandage= {"Anup" : 25, "Vikas" : 29}
print(nameandage)
print(nameandage["Anup"])

# Just like Strings, keys are immutable
# But value object is mutable

# Another way to define Dict
nameandage= [ ("Vikas",20), ("anup",23) ]
nameandage = dict(nameandage)
print(nameandage)


# Adding and updating the Elements
nameandage["anup"]=25
print(nameandage)

nameandage["Priyanka"]=29
print(nameandage)


# Deleting a value in Dict
nameandage.pop("Vikas")
print(nameandage)

nameandage.popitem()
print(nameandage)

del nameandage["anup"]
print(nameandage)

nameandage= {"Ritik" : 21}
print(nameandage)
del nameandage
print(nameandage)
