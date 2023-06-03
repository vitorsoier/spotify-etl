import os
import pandas as pd
import spotipy
import sqlite3
import sqlalchemy

from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("url")
database_location = os.getenv("DATABASE_LOCATION")
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
    df = pd.DataFrame(data)

    # data validation
    if not df["played_at"].is_unique:
        raise Exception("Valor de data não é unico")
    if df.isnull().values.any():
        raise Exception("Valor nulo")

    return df


def load(df):
    engine = sqlalchemy.create_engine(database_location)
    con = sqlite3.connect("spotify.db")
    cur = con.cursor()
    sql_query = """
    CREATE TABLE IF NOT EXISTS spotify(
        played_at VARCHAR(200) PRIMARY KEY,
        artist VARCHAR(200),
        track VARCHAR(200),
        popularity VARCHAR(200)
    )
    """
    cur.execute(sql_query)
    try:
        df.to_sql(name="spotify", con=con, if_exists="append", index=False)
    except:
        print("Dados já existem no banco")
    return print(pd.read_sql("select * from spotify", con))


date = datetime.today() - timedelta(days=2)
raw_data = extract(date)
df = transaform(raw_data)
load(df)
