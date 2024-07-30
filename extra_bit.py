# -------------------------------------------debugging----------------------------------------------
# import pdb
#
#
# def my_func(num1, num2):
#     pdb.set_trace()
#     f = 5 * 121
#     return num1 + num2
#
#
# print(my_func(23,"hey hey"))

# ---------------------------------------Regular-Expressions---------------------------------------

# import re
#
# my_text = "hello again my name is reza how can i help you"
#
# a = re.search("reza", my_text)
# print(f"regular print: {a}")
# print(f"print of span: {a.span()}")
# print(f"print of start: {a.start()}")
# print(f"print of group: {a.group()}")

# ---------------------compile-------------------
# my_text1 = "hello world hello to all around a world 11 60,25 1 01 "
# pattern = re.compile('hello world')
#
# print(pattern.search(my_text1))
# print(pattern.findall(my_text1))
# print(pattern.fullmatch(my_text1))  # when the text exactly same with patter return a match object
# print(pattern.match(my_text1))  # when the one or more char match with text return a match object
#
# pattern1 = re.compile("[0-5][0-9]")
# print(f"print this: {pattern1.findall(my_text1)}")

# --------------------regex-website--------------
# import re
#
# my_email = "www.eza@gmail.com"
# regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
#
# pattern = re.compile(regex)
# print(pattern.fullmatch(my_email))

# --------------------exercise-------------------
import re

text_pattern = r"[a-zA-Z0-9$%#@]{8,}\d$"
my_pattern = re.compile(text_pattern)
while True:
    my_password = input("enter your password:")
    # print(my_pattern.match(my_password))
    summer = my_pattern.match(my_password)
    if "None" != str(summer):
        break
    else:
        print("please enter a correct password")
