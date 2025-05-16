from crewai import Agent
from tools import  FetchMusicTool, FetchLivroTool, FetchCinefiloTool, FetchDicionarioTool, FetchOtakuTool
from config import get_llm

def create_Livreiro_agent():
    return Agent(
        role="Especialista em Livros",
        goal="Recomendar Livros aleatórios ",
        backstory="Você é um especialista em literatura.",
        tools=[FetchLivroTool()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_musico():
    return Agent(
        name="Especialista Musical",
        role="Sugere músicas de acordo com tendências e preferências.",
        goal="Recomendar músicas de diferentes estilos com base no humor ou gosto do usuário.",
        backstory="Um DJ virtual apaixonado por música, treinado para encontrar e sugerir as melhores faixas.",
        tools=[FetchMusicTool()],
        verbose=True,
        llm=get_llm()
    )
def create_cinefilo():
    return Agent(
        role="Especialista em filmes",
        goal="Fornecer filmes pelo gênero",
        backstory="Especialista em cinema.",
        tools=[FetchCinefiloTool()],
        verbose=True,
        llm=get_llm()
    )

def create_dicionario():
    return Agent(
        role="Dicionario ",
        goal="Fala o dicionario do gênero escolhido",
        backstory="Assistente com vasto conhecimento em dicionário Brasileiro.",
        tools=[FetchDicionarioTool()],
        verbose=True,
        llm=get_llm()
    )

def create_otaku():
    return Agent(
        role="Especialista em animes",
        goal="Otaku que sugere um anime com base no gênero fornecido",
        backstory="Otaku com vasto conhecimento em animes.",
        tools=[FetchOtakuTool()],
        verbose=True,
        llm=get_llm()
    )

