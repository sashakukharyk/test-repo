# Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду.
# Контекстний менеджер повинен виводити час, що минув, при виході з контексту.
# Використовуйте контекстний менеджер для вимірювання часу виконання певного фрагменту коду.
# Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора contextmanager
# та за допомогою класу.

# from time import time

# class Timer:

#     def __init__(self) -> None:
#         print("Init method called")

#     def __enter__(self):
#         print("Start")
#         self.time = time()
#         return self.time

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         result = time() - self.time
#         print("End")
#         print(f"Elapsed time: {result}")


# with Timer() as t:
#     for i in range(1, 11):
#         print(i)

# from contextlib import contextmanager
# from time import time

# @contextmanager
# def timer():

#     print("Start")
#     start = time()

#     yield

#     result = time() - start
#     print("End")
#     print("Elapsed time: ", result)

# with timer() as t:
#     for i in range(1,11):
#         print(i)


# Створіть контекстний менеджер DividerContext, який буде прінтити символ, який ми до нього передамо
# як розділитель для основного блоку коду до та після його виконання. Реалізувати контекстний менеджер
# потрібно 2 способами, за допомогою декоратора contextmanager та за допомогою класу.
# (приклад можно знайти у презентації)

# class DividerContext:

#     def __init__(self, char) -> None:
#         self.char = char

#     def __enter__(self):
#         print(self.char * 50)
#         return self.char
    
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print(self.char * 50)

# with DividerContext("$") as d:
#     print("MAIN CODE")

# from contextlib import contextmanager

# @contextmanager
# def DividerContext(char):
    
#     print(char * 50)

#     yield

#     print(char * 50)

# with DividerContext("*") as d:
#     print("MAIN CODE")


# Створіть простий декоратор логування log_func, який буде прінтити будь яке повідомлення
# перед визовом декорованої функції, та після.

# def log_func(func):

#     def inner(*args, **kwargs):
#         print("Будь яке повідомлення перед визовом функції")
#         func(*args, **kwargs)
#         print("Будь яке повідомлення після визову функції")

#     return inner

# @log_func
# def f (a=4, b=7, c=11):
#     print(a, b, c)

# f()


# Реалізувати декоратор timeit, який вимірює час виконання декорованої функції і виводить його.
# Для отримання часу роботи скористуйтесь модулем time і функцією time.time()

# from time import time

# def timeit(func):

#     def inner (*args, **kwargs):
        
#         print("Start")
#         start = time()

#         func(*args, **kwargs)

#         result = time() - start
#         print("Finish")
#         print(result)
    
#     return inner

# @timeit
# def f(argument):

#     for i in argument:
#         print(i)

# f(["word", 4, True, int])


# Створіть декоратор retry який приймає першим аргументом число - кількість разів,
# яку потрібно буде повторити виконання функції у разі викидання нею помилки. 
# (приклад можно знайти у презентації)

import functools

def retry(max_retries):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    return result 
                except ZeroDivisionError as e:
                    print(f"ZeroDivisionError: {e}. Повторна спроба...")
            raise ZeroDivisionError(f"Не вдалося виконати функцію після {max_retries} спроб")

        return wrapper

    return decorator_retry


@retry(max_retries=3)  
def divide(a, b):
    return a / b

try:
    result = divide(10, 0)  
    print(result)
except ZeroDivisionError as e:
    print(f"ZeroDivisionError виконання функції: {e}")
    


# Реалізувати декоратор кешування memoize, який кешує результати декорованої функції
# для покращення продуктивності при повторних викликах з тими самими аргументами. 
# Тобто він повинен запамʼятовувати аргументи з якими функція визивалась і результат 
# роботи функції з цими аргументами. І у випадку, якщо ми вже маємо результат для цих аргументів,
# просто повернути закешований результат, замість виклику функції.

# memory = {}
# def memoize(f):
     
#     def inner(num1, num2):
#         values = set((num1, num2))
#         if values not in memory.values():
#             product = f(num1, num2)
#             memory[product] = values
#             print('result saved in memory')
#             return product
#         else:
#             print('returning result from saved memory')
#             keys = [k for k, v in memory.items() if v == values]
#             return keys
 
#     return inner
     
# @memoize
# def multiply(num1, num2):
#     return num1 * num2
 
# print(multiply(5, 5))
# print(multiply(3, 3))
# print(multiply(10, 7))
# print(multiply(90, 9))
# print(multiply(10, 7)) # directly coming from saved memory
# print(multiply(5, 5)) # directly coming from saved memory






# Створіть декоратор **`rate_limit`**, який обмежує кількість викликів декорованої функції
# протягом певного періоду часу. Декоратор повинен приймати два параметри `max_calls` 
# та `period`. Перший парметр - максимальна кількість допустимих викликів функції.
# Другий параметр - кількість секунд у рамках яких ми можемо зробити `max_calls` викликів. 
# Вам допоможе модуль `datetime` для вирішення цієї задачі.

# import datetime
# from datetime import timedelta
# from time import time

# def fff (max_calls, period):

#     def rate_limit(func):

#         def inner(*args, counter=0, t1 = datetime.datetime.now() + timedelta(seconds=period), **kwargs):
#             while counter < max_calls and datetime.datetime.now() < t1:
#                 func(*args, **kwargs)
#                 counter += 1
#                 print(counter)

#         return inner
#     return rate_limit

# @fff(8000, 3)
# def f():
#     print("Виклик функції")
    
# label = time()
# f()
# result = time() - label
# print("Час який виконувалася функція: ", result)
