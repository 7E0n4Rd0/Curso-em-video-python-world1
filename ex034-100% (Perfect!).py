#exercício 34: Escreva um programa que pergunte o sálario de um funcionário e calcule o.valor do seu aumento.
# para salários superiores a 1.250,00, calcule um aumento de 10%.
# para os inferiores ou iguais, o aumento é de 15%.
salary = float(input('What is the salary for the employee?'))
if salary < 1250.0:
	print('The salary is {} and will increase to {}.'.format(salary, (salary*0.15) + salary))
if salary >= 1250.0:
	print('The salary is {} and will increase to {}.'.format(salary, (salary*0.10) + salary))
#I did in different way, but it's correct!!