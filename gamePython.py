from random import randint
from time import sleep
print('==============  TENTE ADVINHAR O NUMERO!! ============== \n')
numero = 0
n1 = randint(1, 5)
while numero != n1:
   numero = int(input('coloque um numero de 1 a 5: '))
   sleep(1)
   if numero == n1:
      print('O numero foi {}:'.format(n1))
      print ('\n===== PARABÉNS VOCÊ ACERTOU =====')
   elif numero != n1:
      print('Você errou! O Numero Escolhido Foi {}\n '.format(n1))
      print ('===== TENTE NOVAMENTE =====')
print('FIM DE JOGO')
