#I coded thinking was:"Text a code if there's "Santo" in city's name", but It's not this. No attention, made me wrong AGAIN.
'''city = str(input('Digita um nome de uma cidade:'))
city = city.title().strip()
print('Tem "Santo" em;',city,':{}'.format('Santo'in city))'''
#The Correct:
city = str(input('Digita o nome de alguma cidade:'))
city = city.title().strip()
print('Começa com "Santo" o nome da cidade?','{}'.format(city[:5] == 'Santo'))
#I got it to resolved alone with a "base", but this isn't mean I was wrong the code.