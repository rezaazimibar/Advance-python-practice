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
# from functools import reduce  # we should call it at top of code
#
# mylist = [5, 6, 7]
#
#
# def my_accumulator(acc, item):
#     print(acc, item)
#     return acc + item
#
#
# print(reduce(my_accumulator, mylist, 5))

# -------------------------------lambda-expressions-------------------------

# from functools import reduce
#
# print(list(map(lambda item: item * 5, [2, 3, 4, 5, 6])))
#
# print(list(filter(lambda item: item % 5 == 0, [10, 2, 15, 20, 3, 4, 1, 9])))
#
# print(reduce(lambda acc, item: item + acc, [23, 34], 0))

# -----------------------------------exercise--------------------------------

# my_list = [2, 3, 4, 5]
# print(list(map(lambda item: item ** 2, my_list)))
#
# my_tuple = [(1, 2), (2, 1), (8, 9), (10, 4)]
#
# my_tuple.sort(key=lambda item: item[1])
# print(my_tuple)

# -----------------------------comprehensions-----------------------------

# # we can use it on list,set,dictionary
#
# my_list = [char for char in "hello there"]
# my_list1 = [item for item in range(1, 10)]
# my_list2 = [item ** 5 for item in range(1, 10)]
# my_list3 = [item * 7 for item in range(1, 15) if item % 2 != 0]
#
# print(my_list)
# print(my_list1)
# print(my_list2)
# print(f"this going to print just odd numbers: {my_list3}")
#
# # when we want to use it on set
#
# my_set = {char for char in range(1, 10)}
# my_set1 = {item for item in "hey hey"}
#
# print(my_set)
# print(my_set1)
#
# # when we want to use it on dictionary
# my_dict = {
#     'a': 2,
#     'b': 3,
#     'c': 5
# }
#
# my_dict1 = {key: value + 5 for key, value in my_dict.items()}
# my_dict2 = {num: num + 2 for num in [2, 3, 4, 5, 6]}
# print(my_dict1)
# print(my_dict2)

# ---------------------------------exercise--------------------------------

# my_list = ["d", "d", "m", "w", "c", "m"]
#
# my_list1 = list({item for item in my_list if my_list.count(item) > 1})
# print(my_list1)

# -------------------------------extra-bit--------------------------------
# second_list = ["d", "m"]
# translate_list = {char for char in "hey hey Amir"}
# print(translate_list)
