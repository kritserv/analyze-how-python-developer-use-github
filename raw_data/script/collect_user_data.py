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

    response = session.get("https://api.github.com/users/"+username+"/events?per_page=100&page=1")
    print(response)
    event_data = response.json()
    for event in event_data:
        print(event['type'])

#Test function
username_list = ["kritserv"]
for user in username_list:
    CollectDataFromUser(user)
