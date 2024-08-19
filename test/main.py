# def do_stuff(num):
#     try:
#         return int(num) + 5
#     except ValueError as err:
#         return err
#
#
# def lower(num):
#     try:
#         if num:
#             return int(num) + 5
#         else:
#             return "please enter a number"
#     except ValueError as err:
#         return err
#
#
# def adder(num1, num2):
#     return num1 + num2

# -------------------------------------------exercise----------------------------------------------

import random


def game_func(answer, guss):
    if 0 < guss < 11:
        if guss == answer:
            print("you are smart")
            return True
    else:
        print("select another number!!!")
        return False


my_answer = random.randint(1, 10)
if __name__ == "__main__":
    while True:
        try:
            my_guss = int(input("enter a number:"))
            if game_func(my_answer, my_guss):
                break
        except ValueError:
            print("enter a correct number!!")
            continue
