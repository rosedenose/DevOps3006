import math



def rad_con(ang):
    deg = ang * math.pi
    return deg


print(rad_con(6))


def sort_list(list1, sort):
    sorted_list = []
    for x in range(len(list1)):
        sorted_list.append(x)
    if sort == "asc":
        for num1 in list1:
            score = 0
            for num2 in list1:
                if num1 > num2:
                    score = score + 1
            sorted_list[score] = num1
        return sorted_list
    elif sort == "desc":
        for num1 in list1:
            score = 0
            for num2 in list1:
                if num1 < num2:
                    score = score + 1
            sorted_list[score] = num1
        return sorted_list
    elif sort == "none":
        return list1


list2 = [1, 5, 2, 7, 23, 14, 0]
sort2 = "asc"
print(sort_list(list2, sort2))

def dec_to_bin(num):
    iter = 0
    result = 0
    while num != 0:
        rem = num % 2
        result = result + rem * (10 ** iter)
        iter = iter + 1
        num = math.floor(num / 2)
    return result

print(dec_to_bin(24))

def vowel_count(string):
    array = list(string)
    vowel = 0
    for letter in array:
        if letter == "a" or letter == "u" or letter == "i" or letter == "o" or letter == "e":
            vowel = vowel + 1
    return vowel

print(vowel_count("aeoieb"))

def credit_hide(card_num):
    revealed = card_num % 10000
    ast_num = (len(list(str(card_num)))-4)
    ast = "*" * ast_num
    return f"{ast}{revealed}"

print(credit_hide(7854689325468716435))


def ixes_and_oes(string):
    characters = list(string)
    o_count = 0
    x_count = 0
    for character in characters:
        if character == "o" or character == "O":
            o_count = o_count + 1
        elif character == "x" or character == "X":
            x_count = x_count + 1
    if x_count == o_count:
        return True
    else:
        return False

print(ixes_and_oes("xilophne"))


def calculator(num1, op, num2):
    if op == "+":
        result = int(num1) + int(num2)
    elif op == "-":
        result = int(num1) - int(num2)
    elif op == ".":
        result = int(num1) * int(num2)
    elif op == "/":
        result = int(num1) / int(num2)
    return result

print(calculator(6,"-", 3))

def discount(price, discount):
    discount_price = price * discount / 100
    result = price - discount_price
    return result

print(discount(80, 25))

def find_int(list):
    num_list = []
    for x in list:
        q = 0
        try:
            a = x + 1
        except BaseException:
            q = 1
        if q == 0:
            num_list.append(x)
    return num_list

s = [2,"asdfas",24,1,"asfdas"]
print(find_int(s))


def double(string):
    res1 = None
    double_string = []
    characters = list(string)
    for character in characters:
        double_string.append(character)
        double_string.append(character)
    for character in double_string:
        if res1 is None:
            res1 = f"{character}"
        else:
            res1 = f"{res1}{character}"
    return res1

print(double("Aa123!"))