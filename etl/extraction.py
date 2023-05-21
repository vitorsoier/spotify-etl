import base64
import json
import os

from requests import post

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')


def get_token():

    client_string = (client_id + ':' + client_secret).encode('utf-8')
    client_64 = str(base64.b64encode(client_string), 'utf-8')

    url = "https://accounts.spotify.com/api/token"

    headers = {'Authorization': 'Basic ' + client_64}
    payload = {'grant_type': 'client_credentials'}

    result = post(url, headers=headers, data=payload)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token


token = get_token()
print(token)
