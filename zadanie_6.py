# Геращенко Мария Yur`evich
# Variant 5

import random

Trafficlights = [ 'Красный', 'Жёлтый ', 'Зелёный']
VvodTrafficlights=input ('Назовите один из цветов светофора:')
a=random.choice(Trafficlights)
if a==Trafficlights:
print ('Вы угадали! \n Правильный ответ',a)
else:
print('Вы не угадали ! \n Правильный ответ', a)
input ('Нажмите Enter')