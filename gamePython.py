from random import randint
from time import sleep
print('==============  TENTE ADVINHAR O NUMERO!! ============== ')
numero = int(input('coloque um numero de 1 a 5: '))
n1 = randint(1, 5)
sleep(1)
if numero == n1:
   print('O numero foi {}:'.format(n1))
   print ('===== PARABÉNS VOCÊ ACERTOU =====')
elif numero != n1:
   print('O numero foi {}'.format(n1))
   print ('===== VOCÊ ERROU =====')
