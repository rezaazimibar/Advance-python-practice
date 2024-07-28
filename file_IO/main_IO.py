# my_txt = open('my_txt.txt')

# print(f"first time if call it:{my_txt.read()}")
# my_txt.seek(0)
# print(f"second time call with seek(0):{my_txt.read()}")
# my_txt.seek(30)
# print(f"third time call with seek(30):{my_txt.read()}")
# print(f"fourth time call with no seek:{my_txt.read()}")

# print(f"use read line func:{my_txt.readline()}") #read single line
# print(f"use read line func2: {my_txt.readline()}")

# print(f"readLines function: {my_txt.readlines()}")  # read entire line
#
# my_txt.close()  # close the file that we opened top of code

with open('my_txt.txt', mode='a') as my_file:  # standard way to open a IO file
    # mode=r+ mean we can write and read the file or r mean we can only read a file
    # w means we can only write in file
    # a means never write letter from first
    text = my_file.write("new text new life")
    print(text)

with open('my_txt2.txt,', mode='w') as my_file2:  # create a new txt file-
    # -or overwrite the existing file
    text = my_file2.write("new text in new txt file")
