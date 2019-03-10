def get_summ(num_one,num_two):
    try:
        num_one = int(num_one)
        num_two = int(num_two)

        summ = num_one + num_two
        print('Сумма двух чисел равна {}'.format(summ))
    except ValueError:
        print('Введите корректные числа')

num_one = input('Введите первое число: ')
num_two = input('Введите второе число: ')

get_summ(num_one,num_two)