import requests
#print("moshe")
try:
    response = requests.get("htft://github.com")
except BaseException as e:
    print("something went wrong")
    print(e.args)
print("haim")



try:
    f = int(input("enter number: "))
    r = 5/0
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")

#a = int(input("enter number: "))
#b = int(input("enter number: "))
#result = a/b
#print(result)
## ahdhad;fh
# ahfd;dahf;l