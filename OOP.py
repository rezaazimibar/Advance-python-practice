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
#
# class User:
#     def user_connection(self):
#         print(f"{self}logged in")
#
#
# class Dragon(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         print(f"{self.name} fired with {self.power} damaged")
#
#
# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         print(f"{self.name} spell casted with {self.power} damaged per second")
#
#
# player1 = Wizard("gandolf", 33)
# player2 = Dragon("veagar", 500)
# player1.user_connection()
# player1.attack()
# player2.attack()
#
# # ------------isinstance--------------
# # # we use this title when we want to know
# # # something is inheritance of another
# print(isinstance(player1, Wizard))
# print(isinstance(player1, User))
# print(isinstance(User, object))

# ---------------------------------polymorphism-----------------------------------------
#
# # four pillars of OOP encapsulation abstraction inheritance polymorphism
# class Mother:
#     def cheking(self):
#         print("baby was born")
#
#     def talk(self):
#         print("this is the function that belong to mother")
#
#
# class Boy(Mother):
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         Mother.talk(self)
#         print(f"hi my name is {self.name} and i am a boy")
#
#
# class Girl(Mother):
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"hi my name is {self.name} and i am a girl")
#
#
# son1 = Girl("mary")
# son2 = Boy("ahmad")
#
#
# # son1.cheking()
# # son1.talk()
#
#
# # def talk_to_me(char):
# #     char.talk()
# #
# #
# # talk_to_me(son2)
# # talk_to_me(son1)
# #
# # # define with for loop
# #
# # for char in [son1, son2]:
# #     char.talk()
#
# son2.talk()

# ----------------------------------super-()----------------------------------

# class Car:
#     def __init__(self, type):
#         self.type = type
#
#     def buy(self):
#         print("sold out")
#
#
# class BMW(Car):
#     def __init__(self, color, speed, type):
#         Car.__init__(self, type)  # there is two-way to do this one is this and other is in below
#         self.color = color
#         self.speed = speed
#
#
# class Benz(Car):
#     def __init__(self, color, speed, type):
#         super().__init__(type)  # the other way is this use of super()
#         self.color = color
#         self.speed = speed
#
#
# car1 = BMW("red", 342, True)
# car2 = Benz("black", 299, False)
#
# car1.buy()
# print(car1.type)
#
# car2.buy()
# print(car2.type)
#
# # -------introspection---------
#
# print(f"all thing that access to car2 object:{dir(car2)}")


# -----------------------------------dunder-methods---------------------------

# class Toy:
#     def __init__(self, name):
#         self.name = name
#         self.mydict = {
#             "age": 34,
#             "old": True
#         }
#
#     def __str__(self):  # we can change the dunder method usage
#         return f'{self.name}'  # like this
#
#     def __len__(self):
#         return 34
#
#     def __call__(self):
#         return 'we called'
#
#     def __getitem__(self, item):
#         return self.mydict[item]
#
#
# obj1 = Toy("teddy")
# print(obj1.__str__())  # this and below is same
# print(str(obj1))
# print(len(obj1))
# print(f"we called something: '{obj1()}'")  # we can use __call__ like this
# print(obj1["old"])  # use this syntax then we can use __getitem__

# ---------------------------------exercise-------------------------------

# class SuperList(list):
#     def __len__(self):
#         return 100
#
#
# list1 = SuperList()
# list2 = SuperList()
#
# list1.append('apple')
# list2.append(34)
# list2.append(22)
# print(len(list1))
# print(list1)
# print(list2)

# ------------------------------------MRO------------------------------

# class A:
#     num = 2
#
#
# class B(A):
#     num = 5
#
#
# class C(A):
#     num = 8
#
#
# class D(B, C):
#     pass
#
#
# print(D.num)
# print(D.__mro__)  # we can use this key word to know which class chose to inheritance
# print(f' second syntax of mro : {D.mro()} ')
