import requests
import yaml


with open('config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

def find_user_discord(user_id = None, username = None, time = 0, lvl =[1,2,3]):
    url = f"{config['APIURL']}/api/service/promote"
    headers = {
        "Authorization": "Bearer " + config['APIKEY']
    }

    if username:
        data = {
            "Playername": username,
            "Time": time,
            "Level": lvl
        }
    elif user_id:
        data = {
            "Discord_id": user_id,
            "Time": time,
            "Level": lvl
        }    


    
    response = requests.post(url, headers=headers, json=data)

    return response.json()

