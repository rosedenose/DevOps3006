# A
x = 2
y = 3
if x > y:
    print("BIG")
elif x < y:
    print("small")

# B
count = [1, 2, 3, 4, 5]
for i in count:
    print(i)

# C
var = 3
if var == 1:
    print("summer")
elif var == 2:
    print("winter")
elif var == 3:
    print("fall")
elif var == 4:
    print("sprint")

# D
count = 1
while count < 11:
    print(count)
    count = count + 1
# will run 10 times


# E

my_age = 36
first_letter = "K"
usd_to_ils = 3.47
flight_abroad = True
apt_num = 12

print(my_age, first_letter, usd_to_ils, flight_abroad, apt_num)
summ = my_age + usd_to_ils

print(summ)

# F

phone_num = input("please enter your phone number: ")
print(f"Phone number: {phone_num}")


# G

def printHello():
    print("Hello")


printHello()


def calculate():
    sum = 5 + 3.2
    print(sum)


calculate()

# H

name = input("please enter your name: ")


def yourName(name):
    print(name)


def devide(num):
    result = num / 2
    return result


print(devide(3))


# I

def add(num1, num2):
    res = num1 + num2
    return res


def con(str1, str2):
    str = f"{str1} {str2}"
    return str


print(con("hello", "world"))

# K

for int1 in range(6):
    for int2 in range(int1):
        print("#", end='')
    print('')

# or without a nested loop

counts = range(6)

for count in counts:
    print("#" * count)

# L

for i in range(8):
    for j in range(8):
        if i == 1 or i == 7:
            if j == 1 or j == 7:
                print("#", end='')
            else:
                print(" ", end='')
        if i == 2 or i == 6:
            if j == 2 or j == 6:
                print("#", end='')
            else:
                print(" ", end='')
        if i == 3 or i == 5:
            if j == 3 or j == 5:
                print("#", end='')
            else:
                print(" ", end='')
        if i == 4:
            if j == 4:
                print("#", end='')
            else:
                print(" ", end='')
    print('')

# I had a bit of trouble with this one so my first attempt below is not a nested loop solution

h = "#"
counts = [1, 2, 3, 4, 5, 6, 7]
space = " "
for count in counts:
    if count < 4:
        print(f"{space * (count - 1)}{h}{space * (7 - count * 2)}{h}")
    elif count == 4:
        print(f"{space * (count - 1)}{h}")
    elif count > 4:
        print(f"{space * (7 - count)}{h}{space * (5 - (7 - count) * 2)}{h}")


# M
def get_da_namba():
    number = input("Please enter a number: ")
    return number


numba = int(get_da_namba())


def sum_digits(numba):
    res = numba * 10
    digit_sum = 0
    while res > 1:
        digit = numba % 10
        numba = (numba - digit) / 10
        digit_sum = digit_sum + digit
        res = res / 10
    return digit_sum


print(sum_digits(numba))
