import requests

session = requests.Session()
with open ("token.txt", "r") as f:
    x = f.readline()
#session.headers.update({"Authorization": "token "+x.strip()})

def CollectDataFromUser(username):
    response = session.get("https://api.github.com/users/"+username)
    print(response)

    profile_data = response.json()
    followers_count = profile_data["followers"]
    print(followers_count)

#Test function
username_list = ["kritserv"]
for user in username_list:
    CollectDataFromUser(user)
