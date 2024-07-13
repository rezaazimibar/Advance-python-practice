# --------------------------------pure-function-----------------------------
# # there is two rule for create a pure function:
# # 1-in same input always giv same out put 2- do not produce andy side effect
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list  # for example if we write return print(new_list)it-
#     # -going to have side effect
#
#
# print(multiply_by2([3, 4, 5, 6]))


# ------------------------------------map-()-------------------------------
#
# my_list = [2, 3, 4, 5, 6]
#
#
# def power_func(item, power):
#     return item ** power
#
#
# print(list(map(power_func, my_list, [2, 5, 4, 3, 0])))
# print(my_list)

# ---------------------------------filter-()------------------------------

# # check the return
# # if value is true filter going to add that value to the list
#
# numbers = [2, 3, 4, 1, 5, 6]
#
#
# def checker(number):
#     return number % 2 == 0
#
#
# print(f'the number that 2 is: {list(filter(checker, numbers))}')

# ----------------------------------zip-()--------------------------------

# # zip concat lists dict tuple and ect togather
# my_list = [3, 4, 5, 6, 7]
# your_dict = {'h': 23, 'l': 22, 'e': True, 'a': "hey hey", 'b': False}
# his_tuple = (3, 4, 5, 6, 7, 2)
#
# print(list(zip(my_list, your_dict, his_tuple)))

# -------------------------------reduce-()--------------------------------
from functools import reduce  # we should call it at top of code

mylist = [5, 6, 7]


def my_accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(my_accumulator, mylist, 5))
