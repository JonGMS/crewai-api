from crewai import Task

def consultar_cep(agent, cep):
    return Task(
        description=f"Consulte o CEP {cep} e retorne a cidade e estado correspondentes",
        agent=agent,
        expected_output="Nome da Cidade, UF",
        output_file="output/resultado_cep.txt",
        verbose=True
    )

def buscar_clima(agent, contexto):
    return Task(
        description="Obtenha a previsão do tempo para a localidade",
        agent=agent,
        expected_output="Descrição do clima e temperatura em °C",
        output_file="output/previsao_tempo.txt"
    )

def sugerir_roteiro(agent, contexto):
    return Task(
        description="Sugira um roteiro turístico para a cidade, levando em consideração a previsão do tempo",
        agent=agent,
        expected_output="3 sugestões formatadas em tópicos",
        output_file="output/roteiro.txt"
    )

def contar_piada(agent):
    return Task(
        description="Conte uma piada sobre viagens",
        agent=agent,
        expected_output="Uma piada em português",
        output_file="output/piada.txt"
    )