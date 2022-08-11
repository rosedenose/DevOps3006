def print_hello(name):
    '''

    :param name:
    :return:
    '''
    if name != "michael":
        print(f"hello {name}")


print_hello("michael")


def greet_name(name, excluded_name, greeting):
    if name != excluded_name:
        print(f"{greeting} {name}")


def multiply(x, y):
    result = x * y
    # print(result)
    return result


greet_name("Yasha", "michael", "Darova")
bla = multiply(10, 4)
print(bla)


user_name = input("enter your name: ")

print(f"hello {user_name}")