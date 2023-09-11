# Змініть функцію even_odd_generator так, щоб вона генерувала послідовність чисел від 1 до n з рядками "Fizz" для чисел,
# які діляться на 3, "Buzz" для чисел, які діляться на 5, і "FizzBuzz" для чисел, які діляться як на 3, так і на 5.

# def even_odd_generator(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             yield "FizzBuzz"
#         elif i % 3 == 0:
#             yield "Fizz"
#         elif i % 5 == 0:
#             yield "Buzz"
#         else:
#             yield i

# my_generator = even_odd_generator(100)

# while True:
#     try:
#         print(next(my_generator))
#     except StopIteration as e:
#         print(e)
#         break


# Напишіть генератор, який повертає послідовність чисел Фібоначчі.

# def fibonacci_generator():

#     previous_element = 0
#     current_element = 1
#     while True:

#         if previous_element == 0:
#             yield 0

#         yield current_element
#         bufer = current_element
#         current_element += previous_element
#         previous_element = bufer

# fib_gen = fibonacci_generator()

# for i in range(20):
#     print(next(fib_gen))


# Створіть ітератор який буде приймати рядок та кожен виклик методу next() буде повертати наступний символ рядку.


# class NextChar:

#     def __init__(self, string) -> None:
#         self.string = string
#         self.counter = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.counter < len(self.string):
#             char_num = self.counter
#             self.counter += 1
#             return self.string[char_num]
            
#         else:
#             raise StopIteration


# my_string = NextChar("Barcelona > Real")

# print(next(my_string))
# print(next(my_string))
# print(next(my_string))
# print(next(my_string))
# print(next(my_string))
# print(next(my_string))


# Напишіть генератор, який видає послідовність квадратів чисел від 1 до N.

# def square_generator(num):
    
#     for i in range(1, num + 1):
#         yield i * i


# for square in square_generator(5):
#     print(square)


# Реалізуйте ітератор для перебору всіх ключів словника.

# class DictKeysIterator():

#     def __init__(self, dictionary) -> None:
#         self.dictionary = dictionary
#         self.counter = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.counter < len(self.dictionary):
#             char_num = self.counter
#             self.counter += 1
#             return list(self.dictionary.keys())[char_num]
            
#         else:
#             raise StopIteration


# dictionary = {"a": 1, "b": 2, "c": 3}
# dict_iter = DictKeysIterator(dictionary)

# for key in dict_iter:
#     print(key)


# Напишіть генератор, який фільтрує непарні числа з заданої послідовності

# def even_number_filter(numbers):
#     for i in numbers:
#         if i % 2 == 0:
#             yield i

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = even_number_filter(numbers)

# for num in even_nums:
#     print(num)


# Створіть ітератор, який перебирає всі парні числа з заданого діапазону.

# class EvenRangeIterator():

#     def __init__(self, start, end) -> None:
#         self.start = start if start % 2 == 0 else start + 1
#         self.end = end

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start > self.end:
#             raise StopIteration
#         result = self.start
#         self.start += 2
#         return result
         

# even_nums = EvenRangeIterator(1, 23)

# for num in even_nums:
#     print(num)


# Напишіть генератор, який видає послідовність простих чисел.

# def prime_generator():
#     yield 2
#     primes = [2]
#     current = 3
#     while True:
#         is_prime = True
#         for prime in primes:
#             if prime * prime > current:
#                 break
#             if current % prime == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(current)
#             yield current
#         current += 2


# prime_gen = prime_generator()

# for i in range(50):
#     print(next(prime_gen))


# Створіть ітератор, який перебирає всі паліндроми (слова, які читаються однаково зліва направо та зправа наліво) з заданого списку слів.

# class PalindromeIterator():

#     def __init__(self, words) -> None:
#         self.words = words
#         self.counter = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
    
#         while self.counter < len(self.words):
            
#             self.current_word = self.words[self.counter]
#             self.counter += 1
#             if self.current_word == self.current_word[::-1]:
#                 return self.current_word
#         raise StopIteration
                

# words_list = ['level', 'racecar', 'python', 'madam', "kurwa", "amagama"]
# palindrome_iter = PalindromeIterator(words_list)

# for word in palindrome_iter:
#     print(word)
