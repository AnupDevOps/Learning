passwordFile = open('SecretPasswordfile.txt')
secretPassword = passwordFile.read()
print("Enter the password")
typedPassword = input()
if typedPassword == secretPassword:
	print("Access Granted")
	if typedPassword == '12345':
		print('The password is one that an idiot puts on their luggage.')
else:
	print('Access denied')

# ** Exponent 2 ** 3 8
print(2**3)

# % Modules/ remainder 
print(22%4)

# // Integer division/floored quotient 22 // 8 2

print(24//8)