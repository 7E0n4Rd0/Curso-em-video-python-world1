#Desafio 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça o usuário
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
#ou perdeu.
import random
import time
Question_a: str = input('Would like play a game?\n Answers: Yes or No \n').title().strip()
if Question_a == 'Yes':
    print('-=-'*20)
    print('''Ok, follow the instructions:
 I am gonna "think" about a number between 0 and 5
  and you'll guess which number is it.
   If you guess the correct number, you win else you loose.''')
    print('-=-'*20)
if Question_a == 'No':
    print('Bye bye')
    exit()
Question_b = str(input('Are you Ready?\n')).title().strip()
if Question_b == 'Yes':
    print("Let's go!")
    print('-=-'*20)
if Question_b == 'No':
    exit()
value = random.randint(0,5)
Question_c = int(input('Which number is?\n'))
print('Loading...')
time.sleep(2)
print('The number was: {}'.format(value))
if Question_c == value:
    print('You Won')
else:
    print('You Loose')
# random.randint(0, 5) função que randomiza/sorteia números entre 0 e 5.