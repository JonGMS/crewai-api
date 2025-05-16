import requests
import random
from crewai.tools import BaseTool
from typing import Optional
import os

class FetchMusicTool(BaseTool):
    name: str = "Consultor de Músicas"
    description: str = "Sugere músicas aleatórias ou busca informações sobre uma música específica."

    def _run(self, music: str = None) -> str:
        API_KEY = "SUA_CHAVE_AQUI"

        if music:
            url = f"https://api.vagalume.com.br/search.excerpt?q={music}&apikey={API_KEY}"
        else:
            url = f"https://api.vagalume.com.br/hotspots?apikey={API_KEY}"

        response = requests.get(url)
        data = response.json()

        if "mus" in data:
            musica = random.choice(data["mus"])
            return f"Música recomendada: {musica['name']}\nArtista: {musica['band']}\nLink para ouvir: {musica['url']}"
        else:
            return "Não foi possível obter uma recomendação no momento."

class FetchLivroTool(BaseTool):
    name: str = "Consultor de Livros"
    description: str = "Sugere livros com base em um gênero literário aleatório entre opções pré-definidas."

    def _run(self, genero: str = None) -> str:
        generos_disponiveis = ["suspense", "romance", "fantasy", "mystery", "philosophy", "self-help"]
        genero_escolhido = genero if genero else random.choice(generos_disponiveis)

        url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genero_escolhido}&maxResults=5"
        response = requests.get(url)
        data = response.json()

        if "items" in data:
            livro = random.choice(data["items"])["volumeInfo"]
            titulo = livro.get("title", "Sem título")
            autores = ", ".join(livro.get("authors", ["Desconhecido"]))
            return f"Livro recomendado: {titulo}\nAutor(es): {autores}\nGênero: {genero_escolhido.capitalize()}"
        else:
            return "Não foi possível encontrar livros para esse gênero."

class FetchCinefiloTool(BaseTool):
    name: str = "Consultor de Filmes"
    description: str = "Sugere filmes com base em um tema usando a API Simkl."

    def _run(self, tema: str = "drama") -> str:
        API_KEY = "SUA_CHAVE_SIMKL"
        url = f"https://api.simkl.com/search/movie?q={tema}&client_id={API_KEY}"
        headers = {"simkl-api-key": API_KEY}

        try:
            response = requests.get(url, headers=headers)
            data = response.json()

            if isinstance(data, list) and data and "show" in data[0] and "title" in data[0]["show"]:
                filme = data[0]["show"]["title"]
                return f"Filme recomendado sobre '{tema}': {filme}"
            else:
                return "Nenhum filme encontrado para esse tema."
        except Exception as e:
            return f"Erro ao buscar filme: {str(e)}"

class FetchDicionarioTool(BaseTool):
    name: str = "Consultor de Significados"
    description: str = "Fornece a definição de um tema (ex: romance, terror) usando DictionaryAPI.dev."

    def _run(self, termo: str = "romance") -> str:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{termo}"
        response = requests.get(url)
        data = response.json()

        if isinstance(data, dict) and data.get("title") == "No Definitions Found":
            return "Nenhuma definição encontrada."
        significado = data[0]["meanings"][0]["definitions"][0]["definition"]
        return f"Definição de '{termo}': {significado}"

class FetchOtakuTool(BaseTool):
    name: str = "Consultor de Animes"
    description: str = "Sugere animes com base em um tema usando a AniAPI."

    def _run(self, genero: str = "fantasy") -> str:
        API_KEY = "SUA_CHAVE_ANIAPI"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        url = f"https://api.aniapi.com/v1/anime?genres={genero.lower()}&nsfw=false&per_page=5"
        response = requests.get(url, headers=headers)
        data = response.json()

        if data.get("data") and data["data"].get("documents"):
            anime = random.choice(data["data"]["documents"])
            titulo = anime["titles"].get("en", anime["titles"].get("romaji", "Sem título"))
            return f"Anime recomendado com o tema '{genero}': {titulo}"
        else:
            return "Nenhum anime encontrado para esse tema."