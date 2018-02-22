import random, sys

def random_from_to():
	for i in range(5):
		print(random.randint(1,10), sep = ',', end = ' ')

# sys.exit() # == return 0

random_from_to()
random_from_to()
print()

a = '1'
b = 2
c = 3
abc = a * b * c  
spam = [a, b, c, 1, 2, 3, abc, 'abc', "abc"]
del spam[0]
del spam[1]

print(spam[0:len(spam)])

spam_num = [2, 5, 2, 3.14, 1]
spam_num.sort(reverse = True)

while 2 in spam_num:
	spam_num.remove(2)

print(spam_num[:])

eggs = {'name':'a', 'age':'8'}
## key : values

for v in eggs.keys():
	print(v)
for v in eggs.values():
	print(v)

print( eggs.get('ages', -1))	# get
print( eggs.setdefault('ages', -2))		#set

#while True:
#	cin = input()
#	if cin == '':
#		sys.exit()
#	print(cin)

