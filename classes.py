# Створіть клас Rectangle для представлення прямокутника.Додайте методи 
# для обчислення площі та периметра прямокутника. Створіть об'єкт Rectangle і викличте ці методи.

# class Rectangle:
    
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def get_square(self):
#         return self.length * self.width
    
#     def get_perimeter(self):
#         return (self.length + self.width) * 2
    
# rec1 = Rectangle(4,8)
# rec2 = Rectangle(5,10)
# print(rec1.get_perimeter(), rec2.get_perimeter())
# print(rec1.get_square(), rec2.get_square())


# Розробіть клас BankAccount для представлення банківського рахунку. Додайте методи для зняття та поповнення
# коштів на рахунку. Використовуйте магічний метод __str__ для виведення інформації про рахунок.

# class BankAccount:

#     def __init__(self, balance):
#         self.balance = balance

#     def recharge (self, amount):
#         self.balance += amount

#     def withdraw (self, amount):
#         self.balance -= amount

#     def __str__ (self):
#         return f"Current blance is: {self.balance}"
    
# acc1 = BankAccount(10000)
# acc2 = BankAccount(200)

# acc1.withdraw(500)
# acc2.recharge(1200)

# print(acc1)
# print(acc2)


# Розробіть клас Vehicle для представлення транспортного засобу. Додайте атрибути, такі як назва, швидкість і вартість.
# Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю. 
# Створіть список транспортних засобів і відсортуйте його за швидкістю.

# class Vehicle:

#     name = "vehicle"
#     speed = 200
#     price = 10000

#     def __init__(self, name, speed, price):
#         self.name = name
#         self.speed = speed
#         self.price = price

#     def __gt__(self, other):
#         return self.speed > other.speed
    
#     def __str__(self) -> str:
#         return f"{self.name} has speed: {self.speed} and price {self.price}"

# megan = Vehicle("meganchik", 220, 9000)
# camry = Vehicle("3 i 5", 240, 12000)
# audi = Vehicle("audyha", 260, 14000)
# passat = Vehicle("passatik", 230, 11000)

# print(camry.__gt__(megan))
# print(passat.__gt__(audi))

# car_list = [megan, camry, audi, passat]
# car_list.sort(key=lambda x: x.speed)

# for car in car_list:
#     print(car)


# Створіть клас Student для представлення студента. Додайте атрибути, такі як ім'я, прізвище і список оцінок.
# Реалізуйте метод __len__, який повертає кількість оцінок студента. 
# Створіть список студентів і відсортуйте його за кількістю оцінок.

# class Student:
#     name = "default"
#     sourname = "default"
#     marks = []

#     def __init__(self, name, sourname, marks) -> None:
#         self.name = name
#         self.sourname = sourname
#         self.marks = marks

#     def __len__(self):
#         return len(self.marks)
    
#     def __str__(self):
#         return f"{self.name} {self.sourname}"
    
#     def __gt__(self, other):
#         return len(self.marks) > len(other.marks)
    
# stud1 = Student("Robert", "Lewandowski", [5, 4, 5, 5])
# stud2 = Student("Joao", "Felix", [3, 4, 5])
# stud3 = Student("Joao", "Cancelo", [4, 4, 3, 5, 5, 4])
# stud4 = Student("Mark Andre", "Ter Steget", [5, 5, 5, 5, 5, 4, 5, 5])

# sorted_list = sorted([stud1, stud2, stud3, stud4])

# for student in sorted_list:
#     print(student)


# Розробіть клас Library для представлення бібліотеки. А також класс Book для представлення книги.
# Класс Library повинен мати атрибут books зі списком книжок. Кожна книга в бібліотеці має атрибути,
# такі як назва, автор і рік видання. Додайте метод add_book, який додає нову книгу до бібліотеки.
# Реалізуйте метод __str__, який виводить список книг у бібліотеці. Створіть об'єкт Library і додайте кілька книг.
# Виведіть список книг у бібліотеці.

# class Book:

#     name = "default"
#     author = "default"
#     year = 0

#     def __init__(self, name, author, year) -> None:
#         self.name = name
#         self.author = author
#         self.year = year

#     def __str__(self) -> str:
#         return f"{self.name} by {self.author} was written in {self.year} year"
    
# class Library:

#     books = []

#     def __init__(self, books_to_add) -> None:
#         self.books = books_to_add

#     def add_book(self, book):
#         self.books.append(book)

#     def __str__(self) -> str:
#         book_list = "\n".join(str(book) for book in self.books)
#         return f"Library has:\n{book_list}"
    
# book1 = Book("Bookwar", "Did Panas", 1950)
# book2 = Book("Algebra", "Pifagor", 1)
# book3 = Book("Bible", "Jesus", 1999)

# library1 = Library([])
# library1.add_book(book1)
# library1.add_book(book2)
# library1.add_book(book3)

# print(library1)


# Створіть клас Circle, який представляє коло. Реалізуйте методи для обчислення площі та довжини кола.
# Використовуйте аттрибут класу для зберігання значення π (pi).

# class Circle:

#     p = 3.1415926535

#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def get_area(self):
#         return Circle.p * self.radius * self.radius
    
#     def get_circumference(self):
#         return 2 * Circle.p * self.radius
    
# kolo = Circle(8)

# print("Коло має довжину: ", round(kolo.get_circumference(), 2))
# print("Коло має площу: ", round(kolo.get_area(), 2))


# Створіть клас Student, який представляє студента. Реалізуйте атрибут класу для відстеження
# кількості студентів. Для цього змінюйте значення атрибуту класу у методі __init__ .
# Та створіть клас метод для виведення загальної кількості студентів.

# class Student:

#     number_of_students = 0
#     name = "default"
#     sourname = "default"

#     def __init__(self, name, sourname) -> None:
#         self.name = name
#         self.sourname = sourname
#         Student.number_of_students += 1

#     @classmethod
#     def count (sls):
#         return sls.number_of_students
    
# stud1 = Student("Robert", "Lewandowski")
# stud2 = Student("Joao", "Felix")
# stud3 = Student("Joao", "Cancelo")
# stud4 = Student("Mark Andre", "Ter Steget")

# print(Student.count())

# stud5 = Student("Leo", "Messi")

# print(Student.count())


# Створіть клас Book який має такі атрибути як рік видання, назву, автор та кількість сторінок.
# Створіть статік метод який буде приймати список книжок та рік, та повертати кількість книжок
# з цього списку які були опубліковані у цьому році.

# class Book:

#     name = "default"
#     author = "default"
#     year = 0
#     pages = 0

#     def __init__(self, name, author, year, pages) -> None:
#         self.name = name
#         self.author = author
#         self.year = year
#         self.pages = pages

#     @staticmethod
#     def book_this_year(book_list, book_year):
#         count = 0
#         for b in book_list:
#             if b.year == book_year:
#                 count += 1

#         return count
    

# book1 = Book("Bookwar", "Did Panas", 1950, 250)
# book2 = Book("Algebra", "Pifagor", 1999, 362)
# book3 = Book("Bible", "Jesus", 1999, 187)

# book_list = [book1, book2, book3]

# print(Book.book_this_year(book_list, 1999))