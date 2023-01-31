#I'm not sure about the last print...
phrase = str(input('Enter some phrase:')).upper().strip()
print('The letter A appeared {} times;'.format(phrase.count('A')))
print('The first A appeared in position: {};'.format(phrase.find('A')+1))
'''print('The Last letter A appeared in position: {}.'.format(len(phrase)-phrase.count('A')-1))'''
print('The Last letter A appeared in position: {}'.format(phrase.rfind('A')+1))
#I managed to do well in this exercise, I am satisfied.