first_n = int(input("Введите первое число: "))
first_num_count = 0
temp = first_n

while temp > 0:
    first_num_count += 1
    temp = temp // 10

if first_num_count < 3:
    print("В первом числе меньше трёх цифр.")
else:
    last_digit = first_n % 10
    first_digit = first_n // 10 ** (first_num_count - 1)
    between_digits = first_n % 10 ** (first_num_count - 1) // 10
    first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
    print('Изменённое первое число:', first_n)
    second_n = int(input("\nВведите второе число: "))
    second_num_count = 0
    temp = second_n

    while temp > 0:
        second_num_count += 1
        temp = temp // 10
    if second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.")
    else:
        last_digit = second_n % 10
        first_digit = second_n // 10 ** (second_num_count - 1)
        between_digits = second_n % 10 ** (second_num_count - 1) // 10
        second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
        print('Изменённое второе число:', second_n)
        print('\nСумма чисел:', first_n + second_n)