a = input('Введите целое a: ')
b = input('Введите целое b: ')
c = input('Введите целое c: ')
if (a.isdigit() or a[0] == '-' and a[1:].isdigit) \
    and (b.isdigit() or b[0] == '-' and b[1:].isdigit) and \
    (c.isdigit() or c[0] == '-' and c[1:].isdigit):
    x = 3*int(a) + 3 - int(b) + 4*int(c)
    print(f"В результате уравнения x = 3*a + 3 - b + 4*c получилось {x}")
else:
    print('Неверный ввод!')
