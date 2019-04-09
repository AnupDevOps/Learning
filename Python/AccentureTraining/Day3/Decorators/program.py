# Decorators

def test(n):
    return n+1

fun = test
print(test)
print(type(test))
print(type(fun))
print(fun(5))

def testfun(f, val):
    return f(val)

print(testfun(test, 100))
