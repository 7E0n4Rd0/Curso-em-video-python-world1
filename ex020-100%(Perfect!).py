import random
a = input('First Student:')
b = input('Second Student:')
c = input('Third Student:')
d = input('Fourth Student:')
e = input('Fifth Student:')
names = ([a,b,c,d,e])
random.shuffle(names)
print('The order of presentation of the homework will be:{}'.format(names))
