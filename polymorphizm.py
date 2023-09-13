# Напишіть клас "Person", який має властивості name (ім'я) і age (вік). Зробіть ці властивості приватними,
# щоб вони не могли бути змінені напряму ззовні класу. Забезпечте методи для доступу до цих властивостей
#  та встановлення їх значень.

# class Person:

#     def __init__(self, name, age) -> None:
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name
    
#     def get_age(self):
#         return self.__age
    
#     def set_name(self, new_name):
#         self.__name = new_name

#     def set_age(self, new_age):
#         self.__age = new_age
    
# person1 = Person("Dos Santos", 30)

# print(person1.get_age())
# print(person1.get_name())

# person1.set_name("Giovani")
# person1.set_age(34)

# print(person1.get_age())
# print(person1.get_name())


# Розширте клас "Person" з попереднього завдання, додавши методи для зміни значень імені та віку.
# Зробіть так, щоб ім'я не могло містити цифр, а вік був обмежений в діапазоні від 0 до 120.
# При спробі встановити недійсне значення, виведіть повідомлення про помилку.

# import re

# class Person:

#     def __init__(self, name, age) -> None:
#         if re.search("[0-9]", name):
#             print("Error...Name cannot contain digits")
#         else:
#             self.__name = name

#         if 0 < age < 120:
#             self.__age = age
#         else:
#             print("Error...Age should be between 0 and 120")

#     def get_name(self):
#         return self.__name
    
#     def get_age(self):
#         return self.__age
    
#     def set_name(self, new_name):
#         if re.search("[0-9]", new_name):
#             print("Error...Name cannot contain digits")
#         else:
#             self.__name = new_name

#     def set_age(self, new_age):
#         if 0 < new_age < 120:
#             self.__age = new_age
#         else:
#             print("Error...Age should be between 0 and 120")
    
# person1 = Person("Dos Santos", 30)

# print(person1.get_age())
# print(person1.get_name())

# person1.set_name("Giov10ani")
# person1.set_age(120)

# print(person1.get_age())
# print(person1.get_name())


# Розробіть клас "Car", який містить такі властивості: make (марка автомобіля), model (модель автомобіля),
# year (рік випуску автомобіля) і mileage (пробіг автомобіля). Забезпечте можливість доступу до цих властивостей
# через методи, а також зробіть властивості "make" і "model" приватними.

# Додайте метод "drive" до класу "Car", який збільшує пробіг автомобіля на задане значення.
# Перевірте, чи не перевищує пробіг заданий ліміт (наприклад, 300 000 км), і виведіть повідомлення про досягнення
# ліміту при спробі здійснити поїздку.

# class Car:

#     def __init__(self, make, model, year, mileage) -> None:
#         self.__make = make
#         self.__model = model
#         self.year = year
#         self.mileage = mileage # тисяч кілометрів

#     def drive(self, mileage):
#         if self.mileage + mileage < 300:    
#             self.mileage += mileage
#         else:
#             print("Ви досягнули ліміту пробігу")

#     def get_make(self):
#         return self.__make
    
#     def get_model(self):
#         return self.__model
    
#     def get_year(self):
#         return self.year
    
#     def get_mileage(self):
#         return self.mileage
    

# megan = Car("Renault", "Megan", 2012, 216)
# passat = Car("Volkswagen", "Passat", 2015, 200)
# mazda = Car("Mazda", "3", 2007, 150)

# megan.drive(84)
# passat.drive(50)
# mazda.drive(1)

# print(megan.get_mileage())
# print(passat.get_mileage())
# print(mazda.get_mileage())


# Створіть базовий клас "Shape" (фігура), який має властивість color (колір) і метод display_color()
# для виведення коліру фігури. Створіть похідний клас "Rectangle" (прямокутник), який наслідує властивість
# color і додає властивості width (ширина) і height (висота). Забезпечте можливість встановлення значень
# ширини і висоти прямокутника та виведення їх значень.

# class Shape:

#     def __init__(self, color) -> None:
#         self.color = color

#     def display_color(self):
#         print(self.color) 


# class Rectangle(Shape):

#     def __init__(self, color, width, height) -> None:
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def set_width(self, new_width):
#         self.width = new_width

#     def set_height(self, new_height):
#         self.height = new_height

#     def get_width(self):
#         return self.width

#     def get_height(self):
#         return self.height


# rec = Rectangle("Red", 15, 45)

# print(rec.get_height())
# print(rec.get_width())

# rec.set_height(30)
# rec.set_width(70)

# print(rec.get_height())
# print(rec.get_width())


# Розширте клас "Rectangle" з попереднього завдання, перевизначивши метод display_color(). В методі display_color()
# виведіть повідомлення про колір прямокутника і додайте також виведення повідомлення про його розміри (ширину і висоту).

# class Shape:

#     def __init__(self, color) -> None:
#         self.color = color

#     def display_color(self):
#         print(self.color) 


# class Rectangle(Shape):

#     def __init__(self, color, width, height) -> None:
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def display_color(self):
#         return f"Color is {self.color}, width is {self.width}, height is {self.height}"
    

# rec = Rectangle("Green", 70, 80)

# print(rec.display_color())


# class Animal:

#     def __init__(self, title, specie) -> None:
#         self.title = title
#         self.specie = specie

#     def display_info(self):
#         print(f"Animal: {self.title}")
#         print(f"Specie: {self.specie}")
#         print("-" * 70)


# class Mammal(Animal):

#     def __init__(self, title, specie, nutrition) -> None:
#         super().__init__(title, specie)
#         self.nutrition = nutrition

#     def display_info(self):
#         print(f"Animal: {self.title}")
#         print(f"Specie: {self.specie}")
#         print(f"Nutrition: {self.nutrition}")
#         print("-" * 70)

# class Carnivore(Mammal):

#     def __init__(self, title, specie, nutrition, teeth_number) -> None:
#         super().__init__(title, specie, nutrition)
#         self.teeth_number = teeth_number

#     def display_info(self):
#         print(f"Animal: {self.title}")
#         print(f"Specie: {self.specie}")
#         print(f"Nutrition: {self.nutrition}")
#         print(f"Teeth number: {self.teeth_number}")
#         print("-" * 70)

# class Lion(Carnivore):

#     circus_performing = True

#     def __init__(self, title, specie, nutrition, teeth_number, mane_size) -> None:
#         super().__init__(title, specie, nutrition, teeth_number)
#         self.mane_size = mane_size

#     def display_info(self):
#         print(f"Виступає в цирку: {self.circus_performing}")
#         print(f"Animal: {self.title}")
#         print(f"Specie: {self.specie}")
#         print(f"Nutrition: {self.nutrition}")
#         print(f"Teeth number: {self.teeth_number}")
#         print(f"Mane size: {self.mane_size}")
#         print("-" * 70)

# python = Animal("Kaa", "Mammal")
# bear = Mammal("Baloo", "Mammal", "Omnivore")
# tiger = Carnivore("Sher Khan", "Mammal", "Carnivore", 46)
# lev = Lion("Simba", "Mammal", "Carnivore", 38, "Middle")

# python.display_info()
# bear.display_info()
# tiger.display_info()
# lev.display_info()


# Розробіть клас "Square", який успадковує властивості і методи з класу "Rectangle". Додайте властивість side_length
# (довжина сторони) і перевизначте методи, які використовують властивості width і height класу "Rectangle",
# щоб вони використовували властивість side_length класу "Square". Виведіть значення ширини,
# висоти і довжини сторони для об'єкта класу "Square".

# class Shape:

#     def __init__(self, color) -> None:
#         self.color = color

#     def display_color(self):
#         print(f"Color: {self.color}") 


# class Rectangle(Shape):

#     def __init__(self, color, width, height) -> None:
#         super().__init__(color)
#         self.width = width
#         self.height = height

#     def display_color1(self):
#         return f"Color is {self.color}, width is {self.width}, height is {self.height}"
    

# class Square(Rectangle):

#     def __init__(self, color, side_length) -> None:
#         super().__init__(color, side_length, side_length)
#         self.side_length = side_length

#     def display_color(self):
#         return super().display_color()

# sqr = Square("Blue", 8)

# sqr.display_color()
# print(sqr.height)
# print(sqr.width)
# print(sqr.side_length)


class Car:

    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")

class Sedan(Car):

    def __init__(self, make, model, doors) -> None:
        super().__init__(make, model)
        self.doors = doors

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Doors number: {self.doors}")


class SUV(Car):
    
    def __init__(self, make, model, seats) -> None:
        super().__init__(make, model)
        self.seats = seats

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Seats: {self.seats}")

class SportCar(Car):

    def __init__(self, make, model, max_speed) -> None:
        super().__init__(make, model)
        self.max_speed = max_speed

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Max speed: {self.max_speed}")


car1 = Car("Audi", "A4")
auto = Sedan("Mazda", "6", 4)
jeep = SUV("Peugeot", "3008", 5)
lamba = SportCar("Lamorgini", "Gallardo", 320)

car1.display_info()
print("-" * 70)
auto.display_info()
print("-" * 70)
jeep.display_info()
print("-" * 70)
lamba.display_info()