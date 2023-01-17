# number = input('Введите вещественное число: ')
# sum = 0
# for i in number:
#     if i != '.' and i != ',':
#         sum += int(i)
#
# print('Сумма цифр равна: ', sum)
from functools import reduce
number = input('Введите вещественное число: ')
sum1 = [i for i in number if i != '.' and i != ',']
print('Сумма цифр равна: ', reduce(lambda x, y: int(x) + int(y), sum1))
