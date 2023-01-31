salary = float(input('Salary of an employee:'))
increase = salary*(15/100)
new = salary+increase
print('His salary used to be {}, now with the raise he is {:.2f}'.format(salary, new))
