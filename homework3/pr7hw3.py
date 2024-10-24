def do_4(x):
    if x == 0:
        return ''
    else:
        return do_4(x // 4) + str(x % 4)
x = input('Введите целое неотрицательное число: ')
if x.isdigit():
    print(f"Число {x} в 4-ой сс: {do_4(int(x))}")
else:
    print('Неверный ввод!')
