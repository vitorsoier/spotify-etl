# Spotify etl

Nesse projeto vamos simular um processo de etl. Nosso etl vai consistir em quatro etapas:
* Extrair dados da API do spotify
* Tratar esses dados e fazer algumas alterações para gerar insumos de negocios
* Inserir esses dados em um banco de dados relacional
* Automatizar o fluxo utilizando o Airflow

## Extração de dados

Vamos utilizar a API do spotify para fazer a extração dos dados das musicas que escutamos nas ultimas 24hrs. 
Basta visitar esse site e seguir as intruções para gerar sua [chave api](https://developer.spotify.com/documentation/web-api/tutorials/getting-started).
Com ela em mãos vamos realizar o processo de requisição para a API.
Escolhemos utilizar a biblioteca [spotipy](https://spotipy.readthedocs.io/en/2.19.0/#module-spotipy.client) para nos ajudar nesse extração.
Pimeiro precisamos criar um conector autenticado e depois utilizamos o método current_user_recently_played para obter as informações das músicas tocadas recentemente

## Transformação de dados

Quando recebemos os dados temos diversos campos que não são do nosso interesse, por isso vamos pegar apenas 4 campos:
* played_at: timestamp de quando a musica foi reproduzida
* artist: string com o nome do primeiro cantor
* track: string com o nome da musica
* popularity: int com o valor de popularidade da musica
Além disso inseri uma etapa para verificar se temos algum erro no campo played_at ou se existe algo nulo nos nossos dados