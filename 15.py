def get_age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("age cannot be lower than 0")

try:
    get_age()
except ValueError as e:
    if e.args[0] == "age cannot be lower than 0":
        print("your age")