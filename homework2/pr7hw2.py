x = input('Введите целое неотрицательное число: ')
if x.isdigit():
    x_bin = bin(int(x))[2:]
    x_oct = oct(int(x))[2:]
    print(f"Число {x} в 2-ой сс - {x_bin}")
    print(f"Число {x} в 8-ой сс - {x_oct}")
else:
    print('Неправильный ввод!')
