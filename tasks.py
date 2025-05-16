from crewai import Task

def sugerir_Livro(agent ):
    return Task(
        description="Sugira um livro aleatório, falando o genêro do livro",
        agent=agent,
        expected_output="Livros de qualquer procedencia",
        output_file="output/livro_sugerido.txt",
        verbose=True
    )

def sugerir_Musica(agent, contexto):
    return Task(
        description=f"Sugira uma Musica com base no genêro {contexto}",
        agent=agent,
        expected_output="Pode dar 3 musicas",
        output_file="output/musica_sugerida.txt"
    )

def sugerir_Filme(agent, contexto):
    return Task(
        description=f"Sugira um filme com base no genêro {contexto}",
        agent=agent,
        expected_output="3 sugestões formatadas em tópicos",
        output_file="output/filme_sugerido.txt"
    )

def explicar_genero(agent, contexto):
    return Task(
        description=f"Explique esse genêro {contexto}",
        agent=agent,
        expected_output="Entregue o dicionario inteiro desse genêro",
        output_file="output/explicacao_dicionario.txt"
    )

def sugerir_Anime(agent, contexto):
    return Task(
        description=f"Sugira um anime o genêro{contexto}",
        agent=agent,
        expected_output="3 sugestões explicando o motivo da escolha",
        output_file="output/anime_sugerido.txt"
    )
