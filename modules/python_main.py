# # import python1
# import shopping.shopping_cart
# from python1 import multiply, diving  # two different way to import file
# from shopping.another_shopping import another_shopping_file  # good for log address
#
# # from shopping.shopping_cart import add_cart
#
# # two different way to import something
#
# print(multiply(2, 2))
# print(diving(2, 2))
# print(shopping.shopping_cart.add_cart("orange"))
# print(another_shopping_file.power_func(5))

# ---------------------------------------------__main__--------------------------------------------

# from python1 import multiply, diving
# from shopping.another_shopping import another_shopping_file
# from shopping.shopping_cart import add_cart
#
# if __name__ == '__main__':
#     print(f"from python1 module: {diving(23, 22)}")
#     print(f"from python1 module: {multiply(2, 11)}")
#     print(f"in the shopping package import function:{add_cart("apple")}")
#     print(
#         f"inside shopping and inside another_shopping import another_shopping_file imported:"
#         f"{another_shopping_file.power_func(11)} ")
#
# if __name__ == '__main__':  # we can define if when the current file is running-
#     # -because the file can run or import
#     print("if current file is main run this")

# -------------------------------------------built-in-modules--------------------------------------

# import random
#
# # import random as hehe # if we use it we should call hehe instead random
# # this going to rename the module name
#
# # print(random)
# # help(random)
# # print(dir(random))  # show me all available method on this package
#
# print(random.random())
# print(random.randint(23, 44))
# print(random.choice([2, 3, 4, 5, 6, "hey"]))
# my_list = [1, 2, 3, 4, 5, 6, 7]
# random.shuffle(my_list)  # it shuffled my list when ever i run the code
# print(my_list)


# ----------------------sys----------------------
# import random
# import sys
#
# first = sys.argv[1]
# end = sys.argv[2]
# random_num = random.randint(int(first), int(end))
#
# while True:
#     ran_num = input(f"enter the number between {first},{end}:")
#     try:
#         if int(first) <= int(ran_num) <= int(end):
#             if int(ran_num) == random_num:
#                 print("correct answer")
#                 break
#             else:
#                 print("please try again")
#         else:
#             print(f"choose number between {first},{end}")
#     except ValueError:
#         print(f"number error: pleas enter the number between {first},{end} ")

# -----------------------------------------module-install------------------------------------------

# import pyjokes
#
# print(pyjokes.get_joke("en", "neutral"))

# -----------------------------------------Useful-modules------------------------------------------

# from collections import Counter, defaultdict, OrderedDict
#
# my_text = "hey hey my name is reza ha ha ha"
#
# print(Counter(my_text))
#
# my_dict = defaultdict(lambda: 5, {"a": "hey", "b": True})
# print(my_dict["dd"])
# print(my_dict["ddd"])
# print(my_dict)
#
# d = OrderedDict()  # if we change the order of item the equal is false
# # but not in regular object like d={} this going to be True
# d['a'] = 1001
# d['b'] = True
#
# d1 = OrderedDict()
# d1['a'] = 1001
# d1['b'] = True
#
# print(f"is d1 equal to d2:{d1 == d}")

# ---------------data-time-module----------------

# import datetime
#
# print(datetime.time())
# print(datetime.time(5, 33, 22))
# print(datetime.date.today())

# ---------------------array---------------------

# from array import array
#
# my_arr = array("i", [1, 2, 3, 4, 5, 6, 7, 8])
# print(f"print my_arr:{my_arr[5]}")
