#name = input('What is your name?')
#print('It is a pleasure to meet{:=^20}!'.format(name))
n1 = int(input('Enter one value:'))
n2 = int(input('Enter another value:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('The sum is {} \n the multiplication is {} \n the division is {:.3f}, '.format(s,m,d), end ='')
print('The Entire division is {} and the exponentiation is {}'.format(di,e))