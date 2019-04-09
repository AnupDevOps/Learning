print('hello world'.replace('l','b',2))
print('hello' + 'world')
print('3'+'4')

l=[1,2,3]
print(l.append([4,5]))
print('abcdefghijklmnopqrstuvwxyz'.find('jkl'))
print([1,2,3]+[3,2,1])
# print max('hello world')
print([2]*5)
print('example'.find('e'))
print(type(1.0))
print(type(1|2))
print('a' and 'b' and 'c')
print(2**10)
print([x*x for x in range(5)])
print(7>10)
print(4<=4)

print('{} {} {}'.format(10,'hello', True))

print('' and 'b')
print("hello ' world")
print("hello ' worl'd")
print('hello " world')

print('a b c d'.split())

f = None
with open("scores.txt", "r") as f:
	scroe = 0
	for line in f:
		scroe += int(line)
		print(f.closed)
m = [[x,y] for x in range(3) for y in range(4)]
print(len(m))