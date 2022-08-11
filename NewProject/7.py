number = 0

while number < 100:
    number = number + 1
    if (number % 7 == 0) or "7" in str(number):
        continue
    print(number)
else:
    print("string ended successfully")