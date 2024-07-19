# ---------------------------------------iterable-------------------------------

# iterable is any object that we can loop through

# range() is an iterable and also is a generator
# list() is an iterable but not a generator
# in fact anything that are generators it is also an iterable
# but anything that are an iterable not always not a generator

# def generator_func(num):
#     for i in range(num):
#         yield i
#
#
# g = generator_func(100)
# next(g)
# next(g)
# next(g)
# print(next(g))
# for item in generator_func(100):
#     print(item)


# def my_generator_func(num):
#     for i in range(num):
#         yield i
#
#
# generator = my_generator_func(10)
# print(next(generator))
# print(next(generator))

# def my_generator(num):
#     for i in range(num):
#         yield i ** 2
#
#
# generator1 = my_generator(100)
# print(f"my generator is: {next(generator1)}")
# print(f"my generator is: {next(generator1)}")
# print(f"my generator is: {next(generator1)}")
# print(f"my generator is: {next(generator1)}")

# ----------------------------generators-performance----------------------------
from time import time


def performance(func):
    def warp_func(*args, **kwargs):
        time1 = time()
        func(*args, **kwargs)
        time2 = time()
        print(f"the time is: {time2 - time1}")

    return warp_func


@performance  # generators are faster than regular iterable
def my_generator(num):
    print("1)")
    for i in range(num):
        i * 5


@performance
def my_iterable(num):
    print("2)")
    for i in list(range(num)):
        i * 5


my_generator(100000000)
my_iterable(100000000)
