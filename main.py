# Первый блок
print('Hi, PyCharm')
x = 43
y = 32
print(x * y)
print("End line")

# 1st program
print(9 ** 0.5 * 5)  # Верно?

# 2nd program
print(9.99 > 9.98, 1000 != 1000.1)  # Верно?

# 3rd program
print(2 * (2 + 2))  # без приоритета
print(2 * 2 + 2)  # с приоритетом
print(2 * (2 + 2) == 2 * 2 + 2)  # результат сравнения

# 4th program
num_given = '123.456'  # Вывести на экран первую цифру после запятой - 4
withdraw_part = num_given.split('.')[1]  # Вывести на экран первую цифру после запятой - 4
print(withdraw_part[0])  # Вывести на экран первую цифру после запятой - 4

number_str = '123.456'  # Преобразуйте строку в дробное число. ('123.456' -> 123.456)
number = float(number_str)  # Преобразуйте строку в дробное число. ('123.456' -> 123.456)

num_str = '123.456'  # Умножьте на 10, чтобы сместить 4 в целую часть
num_float = float(num_str)  # Умножьте на 10, чтобы сместить 4 в целую часть
num_shifted = num_float * 10  # Умножьте на 10, чтобы сместить 4 в целую часть
result = int(num_shifted) % 10  # Умножьте на 10, чтобы сместить 4 в целую часть
print(result)  # Умножьте на 10, чтобы сместить 4 в целую часть