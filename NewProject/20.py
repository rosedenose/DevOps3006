import requests
response = requests.get("http://localhost:5001")
if response.text == "hello and welcome to the world of games":
    print("all is good")
else:
    print("all is bad")

