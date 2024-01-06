import requests

username = "kritserv"

session = requests.Session()
#session.headers.update({"Authorization": "token {token}"})
response = session.get("https://api.github.com/users/"+username)
print(response)

profile_data = response.json()
followers_count = profile_data["followers"]
print(followers_count)
