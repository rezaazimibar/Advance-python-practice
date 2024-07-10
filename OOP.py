# -----------------------------------------OOP------------------------------------

# class MyClass:
#     pass
#
#
# obj1 = MyClass()
# obj2 = MyClass()
#
# print(type(3432))
# print(type("hey hey"))
# print(type(True))
# print(f"this is the main class with out () '{type(MyClass)}'")
# print(f"this is the obj from class:         '{type(obj1)}'")
# print(f"this is the another obj from class: '{type(obj2)}'")

# -------------------------------------creating-our-own-object------------------------

# class NameCharacter:
#     membership = True  # class object attribute
#
#     def __init__(self, name, age):
#         self.name = name  # attributes
#         self.age = age
#
#     def run(self):
#         print("run")
#
#
# player1 = NameCharacter("reza", 55)
# player2 = NameCharacter("hossein", 34)
# player2.attack = 50
#
# print(player1.age)
# print(player2.run())
# print(player2.attack)
# print(player2.membership)

# -------#new calss------

# class Friends():
#     is_friends = True
#
#     def __init__(self, name, age):
#         if Friends.is_friends:
#             self.name = name
#             self.age = age
#
#     def laugh(self, extra):
#         print(f"he he he {self.name} was laugh. {extra}")
#         return "they laughed"
#
#     @classmethod  # with this we can create object form main class
#     def creator_char(cls, name, num1, num2):  # we can also use it as a object creator
#         return cls(name, num1 + num2)
#
#     @staticmethod  # this is just static method
#     def static_method(num2, num3):
#         return num3 + num2
#
#
# character1 = Friends("joyi", 25)
# character2 = Friends("phebe", 24)
# character3 = Friends.creator_char("reza", 3, 20)
#
# print(f'third char age: {character3.age}')
# print(f'third char name: {character3.name}')
# print(character2.laugh("and done"))
# print(character2.name)
# print(Friends.creator_char("hossein", 2, 10))  # we can also show this because this is the static methon
# print(f"third char use static method{character3.static_method(34, 23)}")

# #new class

# class Cars:
#     madeIn = "Germany"
#
#     def __init__(self, model, speed, color):
#         self.model = model
#         self.speed = speed
#         self.color = color
#
#     def run(self):
#         return self
#
#     def intro(self):
#         print(
#             f"""the model of car is {self.model}
# and maximum speed of this car is {self.speed}km/h
# and it color is {self.color} that make in {Cars.madeIn}""")
#
#
# bmw1 = Cars("BMW", 250, "red")
# print(f"when we run the car {bmw1.run()}")
#
# print(type(34))
#
# bmw1.intro()

# ----------------------------------------private-vs-public-----------------------------------------

# class SportBall:
#     isSportBall = True
#
#     def __init__(self, name, color):
#         self._name = name  # this is the standard that say to other programmer this is the private method
#         self.color = color  # but you can change the variable as well
#
#     def intro(self):
#         print(f"this is a {self._name} ball that it color is {self.color}")
#         return "hey hey"
#
#
# ball1 = SportBall("football", "whit,black")
# ball1.color = "blue"
# print(ball1._name)
# print(ball1.color)
# ball1.intro()

# ----------------------------------inheritance----------------------------

class User:
    def user_connection(self):
        print(f"{self}logged in")


class Dragon(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} fired with {self.power} damaged")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} spell casted with {self.power} damaged per second")


player1 = Wizard("gandolf", 33)
player2 = Dragon("veagar", 500)
player1.user_connection()
player1.attack()
player2.attack()

# ------------isinstance--------------
# # we use this title when we want to know
# # something is inheritance of another
print(isinstance(player1, Wizard))
print(isinstance(player1, User))
print(isinstance(User, object))
