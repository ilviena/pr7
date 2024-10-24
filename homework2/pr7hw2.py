x = input('Введите целое число: ')
if x[0]=='-' and x[1:].isdigit():
    x_bin = '-' + bin(int(x))[3:]
    x_oct = '-' + oct(int(x))[3:]
    print(f"Число {x} в 2-ой сс - {x_bin}")
    print(f"Число {x} в 8-ой сс - {x_oct}")
elif x.isdigit():
    x_bin = bin(int(x))[2:]
    x_oct = oct(int(x))[2:]
    print(f"Число {x} в 2-ой сс - {x_bin}")
    print(f"Число {x} в 8-ой сс - {x_oct}")
else:
    print('Неправильный ввод!')
