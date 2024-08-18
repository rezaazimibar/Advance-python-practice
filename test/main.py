def do_stuff(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err


def lower(num):
    try:
        if num:
            return int(num) + 5
        else:
            return "please enter a number"
    except ValueError as err:
        return err


def adder(num1, num2):
    return num1 + num2
