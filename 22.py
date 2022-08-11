import requests
response = requests.get("https://api.github.com/users/avielb/repos")
result = []

for repo in response.json():
    result.append(repo["full_name"])
#short
result = [repo["full_name"] for repo in response.json() if "first" in repo["full_name"]]

