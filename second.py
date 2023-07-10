while True:
    command = input("Выберите операцию: ")
    if command in "+-*/":
        break
    print("Ошибка: такой операции не существует. Попробуйте ещё раз.")

count_of_operations = int(input("Сколько операндов? "))
result_str = ''
result = 0
for count in range(1, count_of_operations + 1):
    number = int(input(f"Введите число {count}: "))

    if command == "+":
        result += number
    elif command == "-":
        result -= number
    elif command == "*":
        result *= number
    elif command == "/":
        result /= number

    if count != count_of_operations:
        if count != 1:
            result_str += " "
        result_str += str(number) + " " + command
    else:
        result_str += " " + str(number) + " = " + str(result)

print(result_str)