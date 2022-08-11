# 1
# 2
try:
    a = 1 / 0
except ZeroDivisionError:
    print("cannot divide by zero")

# 3
try:
    x = 1
finally:
    print('finally')

# code thrown an exception the "finally" in the print function should have been in '' and not in ""

# 4

try:
    c = 5 / 0
    prift("blabla")
except:
    print("found an issue")

# this exception handler catches all possible issues that can come in try
# 5
# this exception handler is too general and it is hard for us to debug using only this

# 6

try:
    open("")
    d = 4 / 0
except IOError:
    print("please enter the proper file name")
except ZeroDivisionError:
    print("you divided by zero and created a black hole, now we're all doomed!!")

# 7,8
my_file = open("words.txt", "w")
my_file.write("Alexey\nAlexey Kagansky")
my_file.close()

my_file = open("words.txt")
for line in my_file.readlines():
    print(line)
my_file.close()

# -*- coding: utf-8 -*-

my_file = open("words.txt", "w", encoding='UTF-8')
my_file.write("קוראים לי אלכסיי")
my_file.close()

my_file = open("words.txt", encoding='UTF-8')
for line in my_file.readlines():
    print(line)
my_file.close()
