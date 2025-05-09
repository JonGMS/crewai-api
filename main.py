from crewai import Crew
from agents import *
from tasks import *
from dotenv import load_dotenv

load_dotenv()

# Configuração
cep = "88504480"

# Cria agentes
localizador = create_cep_agent()
meteorologista = create_meteorologista()
consultor = create_consultor_viagens()
comediante = create_comediantes()

# Cria tarefas
task1 = consultar_cep(localizador, cep)
task2 = buscar_clima(meteorologista, [task1])
task3 = sugerir_roteiro(consultor, [task1])
task4 = contar_piada(comediante)

# Configura Crew
crew = Crew(
    agents=[localizador, meteorologista, consultor, comediante],
    tasks=[task1, task2, task3, task4],
    verbose=True
)

# Execução
print("## Agente Turístico Iniciado ##")
resultado = crew.kickoff()

print("\n=== RESULTADOS ===")
print(resultado)