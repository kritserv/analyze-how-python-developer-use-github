import requests

session = requests.Session()
#session.headers.update({"Authorization": "token {token}"})

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
