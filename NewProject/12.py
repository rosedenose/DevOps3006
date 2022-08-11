

def save_name():
    my_file = open("names.txt", "a")
    current_name = input("enter your name: ")
    my_file.write(current_name + "\n")
    my_file.close()

def show_name():
    my_file = open("names.txt")
    for name in my_file.readlines():
        print(name, end='')
    my_file.close()

print(show_name())


for i in range(5):
    save_name()
show_name()

with open("names.txt") as my_file:
    for name in my_file.readlines():
        print(name.strip())