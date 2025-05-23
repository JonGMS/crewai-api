from crewai import Crew
from agents import *
from tasks import *
from dotenv import load_dotenv

load_dotenv()

# Configuração
#cep = "88509900" #Coloquei o CEP da Uniplac para n me expor tanto 

# Cria agentes
livreiro = create_Livreiro_agent()
cinefilo = create_cinefilo()
otaku = create_otaku()
dicionario = create_dicionario()
musico = create_musico()

# Cria tarefas
genero = sugerir_Livro(livreiro)
task2 = explicar_genero	(dicionario, [genero])
task3 = sugerir_Filme(cinefilo, [genero])
task4 = sugerir_Anime(otaku, [genero])

#task5 = sugerir_Musica(musico, [genero])

# Configura Crew
crew = Crew(
    agents=[livreiro,dicionario, cinefilo, otaku, musico],
    tasks=[genero, task2, task3, task4],
    verbose=True
)

# Execução
print("## Agentes Iniciados ##")
resultado = crew.kickoff()

print("\n=== RESULTADOS ===")
print(resultado)