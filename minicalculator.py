from math import *

user_number1 = float(input('Введите первое число: '))
user_number2 = float(input('Введите второе число: '))

print('Список доступных операций: +, -, x, степень, корень')
choose_operation = input('Введите операцию из списка выше: ')

# Основная программа
if choose_operation == '+':
    print(f'Сумма: {user_number1 + user_number2}')
elif choose_operation == '-':
    print(f'Разность: {user_number1 - user_number2}')
elif choose_operation == 'x':
    print(f'Произведение: {user_number1 * user_number2}')
elif choose_operation == 'степень':
    print(f'Степень: {user_number1 ** user_number2}')
elif choose_operation == 'корень':
    print(f'Корень: {sqrt(user_number1)}')
else:
    print('Недопустимая операция.')

# Цикл с завершением программы
input()