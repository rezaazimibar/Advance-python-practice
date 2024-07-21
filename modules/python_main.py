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

import random

# import random as hehe # if we use it we should call hehe instead random
# this going to rename the module name

# print(random)
# help(random)
# print(dir(random))  # show me all available method on this package

print(random.random())
print(random.randint(23, 44))
print(random.choice([2, 3, 4, 5, 6, "hey"]))
my_list = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(my_list)  # it shuffled my list when ever i run the code
print(my_list)
