import requests
import yaml


with open('config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

def find_user_discord(user_id = None, username = None):
    url = f"{config['APIURL']}/api/service/user"
    headers = {
        "Authorization": "Bearer " + config['APIKEY']
    }
    if user_id:
        data = {
            "Discord_id": user_id
        }
    elif username:
        data = {
            "Playername": username
        }
    
    response = requests.post(url, headers=headers, json=data)

    return response.json()

