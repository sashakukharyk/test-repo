# Обробіть виняток IndexError, коли програма намагається отримати доступ до неправильного індексу в списку.

# l = ["string", 1, True, ""]

# try:
#     print(l[len(l)])

# except IndexError as e:
#     print(e)


# Створіть функцію, яка приймає два числа від користувача та обробляє помилку, якщо введені дані не є числами.

# try:
#     first_num = int(input("Enter first number: "))
#     second_num = int(input("Enter second number: "))

# except ValueError as e:
#     print(e)


# Напишіть програму, яка відкриває файл для читання та обробляє помилку FileNotFoundError, якщо файл не знайдено.

# import os

# try:
#     f = open("file_which_doesn`t_exist.txt", "r")

# except FileNotFoundError as e:
#     print(e)

# else:
#     print(f.read())


# Реалізуйте функцію, яка ділить два числа, але обробляє помилку **`ZeroDivisionError`**, якщо друге число дорівнює нулю.

# first_num = 100
# second_num = int(input("Enter a number: "))

# try:
#     print(first_num / second_num)

# except ZeroDivisionError as e:
#     print(e)

# else:
#     print("Great success")


# Напишіть програму, яка читає вміст текстового файлу та виводить кількість слів у ньому.

# f = open("file.txt", "r")
# l = list(f.read().split())
# print(len(l))
# f.close()


# Створіть функцію, яка приймає рядок від користувача та записує його у файл.

# string = input("Enter a text: ")
# f = open("file_to_write.txt", "a+")
# f.write(string)
# f.close()


# Реалізуйте програму, яка копіює вміст одного файлу в інший.

# f = open("file.txt", "r+")
# f1 = open("file_to_write.txt", "w+")
# f1.write(str(f.read()))

# f.close()
# f1.close()


# Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст,
# виводячи рядки, які є у першому файлі, але відсутні у другому.

# f = open("file.txt", "r")
# f1 = open("file_to_write.txt", "r")

# for line in f:
#     if line not in f1:
#         print(line)

# f.close()
# f1.close()


# Створіть функцію, яка видаляє вказаний рядок з текстового файлу.

# f = open("file_to_write.txt", "r")
# string = input("Enter a line you want to remove from file: ")
# lines = f.readlines()
# f.close()
# f = open("file_to_write.txt", "w")

# for line in lines:
#     if line != string + "\n":
#         f.write(line)

# f.close()

