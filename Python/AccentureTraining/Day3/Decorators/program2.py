def parentFun(num):

    def childfun():
        print("Hello from Child 1")
 
    def childfun2():
        print("Hello from Child 2")

    if num > 10:
        return childfun
    else:
        return childfun2

# Focus on below lines

op = parentFun(100)

op()

print(".................... Checking Second condition ...................")

op = parentFun(8)

op()

