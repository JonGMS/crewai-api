import requests
import random
from crewai.tools import BaseTool
from typing import Optional
import os

import requests
import random
from crewai.tools import BaseTool
from pydantic import BaseModel




class FetchMusicTool(BaseTool):#não esta sendo utilizado
    name: str = "Consultor de Músicas"
    description: str = "Sugere músicas com base em um gênero musical usando a API do Last.fm."

    def _run(self, music: Optional[str] = None) -> str:
        genero = music if music else "pop"

        url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={genero}"
        response = requests.get(url)
        data = response.json()

        if "tracks" in data and "track" in data["tracks"]:
            faixa = random.choice(data["tracks"]["track"])
            titulo = faixa["name"]
            artista = faixa["artist"]["name"]
            link = faixa["url"]
            return f"Música recomendada: {titulo}\nArtista: {artista}\nLink: {link}"
        else:
            return "Não foi possível obter uma recomendação no momento."

class FetchLivroTool(BaseTool):
    name: str = "Consultor de Livros"
    description: str = "Sugere um livro com base em um gênero literário aleatório entre opções pré-definidas."

    def _run(self, genero: str = None) -> str:
        generos_disponiveis = ["suspense", "romance", "fantasy", "mystery", "philosophy", "self-help"]
        genero_escolhido = genero if genero else random.choice(generos_disponiveis)

        url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genero_escolhido}&maxResults=1"
        response = requests.get(url)
        data = response.json()

        if "items" in data and len(data["items"]) > 0:
            return f"Gênero do livro: {genero_escolhido.capitalize()}"
        else:
            return "Não foi possível encontrar livros para esse gênero."

class FetchCinefiloTool(BaseTool):
    name: str = "Consultor de Filmes"
    description: str = "Sugere filmes com base em um tema usando a API Simkl."

    def _run(self, tema: str = "drama") -> str:
        url = f"https://api.simkl.com/search/movie?q={tema}"

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
        genero_lower = genero.lower()

        url = f"https://api.jikan.moe/v4/anime?genres={genero_lower}&limit=10"
        response = requests.get(url)
        if response.status_code != 200:
            return "Erro ao consultar a API de animes."

        data = response.json()
        animes = data.get("data", [])

        if not animes:
            return f"Nenhum anime encontrado para o gênero '{genero}'."

        anime = random.choice(animes)
        titulo = anime.get("title", "Sem título")

        return f"Anime recomendado com o tema '{genero}': {titulo}"