# -------------------------------------------debugging----------------------------------------------
import pdb


def my_func(num1, num2):
    pdb.set_trace()
    f = 5 * 121
    return num1 + num2


print(my_func(23,"hey hey"))