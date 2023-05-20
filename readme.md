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