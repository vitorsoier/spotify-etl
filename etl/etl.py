import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta
import os

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("url")

scope = "user-read-recently-played"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
    )
)


def extract(date, limit=50):
    """Pega as ultimas musicas tocadas

    ARGS:
        date(datetime): Data da busca
        limit (int): Limite de elementos retornados da busca
    """
    ds = int(date.timestamp()) * 1000
    return sp.current_user_recently_played(limit=limit, after=ds)


def transaform(raw_data):
    data = []
    for info in raw_data["items"]:
        data.append(
            {
                "played_at": info["played_at"],
                "artist": info["track"]["artists"][0]["name"],
                "track": info["track"]["name"],
                "popularity": info["track"]["popularity"],
            }
        )
    return data


date = datetime.today() - timedelta(days=1)
raw_data = extract(date)
data = transaform(raw_data)
print(data)
