# workday = 5
# day_list = [1,2,3,4,5,6,7]
# for i in range(7):
#     day = int(input(('Введите число от 1 до 7',i,': ')))
#     if day > workday:
#         print('Да')
#     else:
#         print('Нет')

day1 = int(input(('Введите число от 1 до 7: ')))
day_list = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
days = [i for i, val in enumerate(day_list, start=1)]
day2 = ['Да' if day1 > 5 else 'Нет']
print(day2)

