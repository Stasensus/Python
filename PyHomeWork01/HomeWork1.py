a = int(input('Введите порядковый номер дня недели:'))
if 0 < a < 6:
    print('Это трудовые будни...')
elif 5 < a < 8:
    print('Это законный выходной')
else:
    print('Нет такого дня недели')