#I tried to do this exercise, but happend the same problem "Limitation on the code".
'''number = str(input('Enter some number of 0 to 9999:'))
print('Unit: {}'.format(number[3]))
print('Ten: {}'.format(number[2]))
print('Hundred: {}'.format(number[1]))
print('Thousand: {}'.format(number[0]))'''
num = int(input('Enter some number:'))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('Analysing the number {}'.format(num))
print('Unit: {}'.format(u))
print('Ten: {}'.format(d))
print('Hundred: {}'.format(c))
print('Thousand: {}'.format(m))
#Well I tried and happend the same shit again