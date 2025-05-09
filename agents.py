from crewai import Agent
from tools import FetchAddressTool, FetchWeatherTool, FetchJokeTool
from config import get_llm

def create_cep_agent():
    return Agent(
        role="Especialista em CEP Brasileiro",
        goal="Identificar cidades e estados a partir de CEPs",
        backstory="Você é um especialista em geografia brasileira com vasto conhecimento sobre códigos postais.",
        tools=[FetchAddressTool()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_meteorologista():
    return Agent(
        role="Meteorologista",
        goal="Fornecer previsões climáticas precisas",
        backstory="Especialista em análise atmosférica.",
        tools=[FetchWeatherTool()],
        verbose=True,
        llm=get_llm()
    )

def create_consultor_viagens():
    return Agent(
        role="Consultor de Turismo IA",
        goal="Responder dúvidas sobre viagens usando Groq",
        backstory="Assistente com vasto conhecimento em destinos turísticos globais.",
        verbose=True,
        llm=get_llm()
    )

def create_comediantes():
    return Agent(
        role="Comediante de Viagens",
        goal="Descontrair com piadas sobre turismo",
        backstory="Humorista especializado em anedotas sobre viagens.",
        tools=[FetchJokeTool()],
        verbose=True,
        llm=get_llm()
    )