# -------------------------------error-handling-----------------
# while True:
#     try:
#         age = input("Enter your name? ")
#         print(1403 - int(age))
#     except ValueError:
#         print("please enter the correct number")
#     else:
#         print("thank you")
#         break


# def my_mixer(num1, num2):
#     try:
#         return num1 / num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(f"please enter the right number bro your error is {err}")
#
#
# print(my_mixer(23, 0))

# while True:
#     try:
#         age = int(input("say your age:"))
#         print(10 / age)
#         raise OverflowError("i am a value error")
#     except ValueError:
#         print("pleas enter the correct number")
#
#     except ZeroDivisionError:
#         print("do not enter a zero as a number")
#     except OverflowError as err:
#         print(f"error box of over flow {err}")
#     # else:
#     #     print("thank you")
#     #     break
#     finally:
#         print("end of code done")
#     # print("ohhh") #never run if we use break in finally
