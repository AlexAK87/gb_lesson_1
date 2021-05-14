
number = input('Введите число от 0 до 20 или введи / для проверки ')

if number == "/":
    i = 0
    while i != 21:
        if i == 1:
            print('{} процент'.format(i))
        elif i >= 2 and i <= 4:
            print('{} процента'.format(i))
        else:
            print('{} процентов'.format(i))
        i += 1
elif number == '1':
    print('{} процент'.format(number))
elif number >= '2' and number <= '4':
    print('{} процента'.format(number))
else:
    print('{} процентов'.format(number))