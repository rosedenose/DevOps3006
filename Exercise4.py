import ast
import requests
import names
from selenium import webdriver

#1
response = requests.get("https://api.github.com/users/avielb/repos")
result = []

for repo in response.json():
    result.append(repo["full_name"])

if len(result) >= 5:
    print("there are 5 or more repositories in this link\n")
else:
    print("there are less than 5 repositories in this link\n")


#2

response=[]
for i in range(3):
    random_name = names.get_first_name()
    response = requests.get(f"https://api.agify.io/?name={random_name}")
    dict = ast.literal_eval(response.text)
    if 0 <= dict["age"] <= 120:
        print(f"{random_name} is {dict['age']}")
    else:
        print(f"{dict['age']} is not within parameters")

#3

response = requests.get("http://universities.hipolabs.com/search?country=israel")
result = []

for repo in response.json():
    result.append(repo["name"])

if len(result) >= 5:
    print("there are 5 or more universities in this link\n")
else:
    print("there are less than 5 universities in this link\n")

#4

my_driver = webdriver.Chrome("chromedriver.exe")

my_driver.get("https://www.ycombinator.com")
page_title = my_driver.title

if page_title == "Y Combinator":
    print("the tile is correct\n")
else:
    print("the title is incorrect\n")

#5

hub_driver = webdriver.Chrome("chromedriver.exe")

hub_driver.get("https://hub.docker.com")
hub_title = hub_driver.title

if hub_title == "Docker Hub Container Image Library | App Containerization":
    print("the tile is correct\n")
else:
    print(f"the title is incorrect, the title is {hub_title}\n")

