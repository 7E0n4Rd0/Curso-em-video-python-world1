#First algorithm example using If and else.
'''name = str(input('Qual é o seu nome?'))
if name == 'Leonardo':
    print('Que nome Top!!!')
else:
    print('Nome simples >:[')
print('Tenha um Bom dia, {} :)'.format(name))'''
#Second example:
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('Sua média foi: {:.1f}'.format(m))
if m >=6.0:
    print('Sua nota está acima da média. Ótimo!')
else:
    print('Sua nota está abaixo da média. ESTUDA MAIS!!!')