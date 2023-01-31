#Escreva um programa que leia a velocidade de um carro. Se ele ultrapasssar 80km/h, mostre a mensagem que ele foi multa-
#do. A multa vai custar RS7,00 por Km acima do limite.
import time
print('-=-'*40)
print('Havia um sujeito em seu carro passando pela estrada, o motorista dirigia sem preocupar em olhar no metrônomo.')
time.sleep(6)
print('Portanto, ele aproximava de um radar eletrônico, ele pisou no freio e passou em uma certa velocidade.')
time.sleep(6)
print('-=-'*40)
time.sleep(1)
velocidade = int(input('Qual foi a velocidade que ele passou pelo radar?\n'))
if velocidade <= 80:
    print('O Sujeito passou pelo radar sem ser multado.')
else:
    multa = (velocidade-80)*7
    print('O Sujeito passou pelo radar com a velocidade acima do limite e teve que pagar {} reais de multa'.format(multa))
