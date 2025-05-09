import requests
from crewai.tools import BaseTool
from typing import Optional
import os

class FetchAddressTool(BaseTool):
    name: str = "Consultor de CEP"
    description: str = "Obtém cidade e estado a partir de um CEP brasileiro."
    cep: Optional[str] = None  # Adicionando tipo explícito

    def _run(self, cep: str) -> str:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        data = response.json()
        return f"CEP: {cep}\nCidade: {data['localidade']}\nEstado: {data['uf']}"
    
class FetchWeatherTool(BaseTool):
    name: str = "Meteorologista"
    description: str = "Obtém a previsão do tempo para uma cidade."

    def _run(self, local: str) -> str:
        api_key = os.getenv("OPENWEATHER_API_KEY")
        cidade, estado = local.split(", ")

        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={cidade},{estado},BR&appid={api_key}&lang=pt&units=metric"
        )
        data = response.json()
        return f"{data['weather'][0]['description']}, {data['main']['temp']}°C"
    
class FetchJokeTool(BaseTool):
    name: str = "Contador de Piadas"
    description: str = "Conta piadas sobre viagens."

    def _run(self) -> str:
        response = requests.get("https://v2.jokeapi.dev/joke/Travel?lang=pt")
        data = response.json()
        if data["type"] == "twopart":
            return f"{data['setup']}\n{data['delivery']}"
        return data["joke"]