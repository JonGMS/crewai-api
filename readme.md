# 📚🎶 Agente de Recomendações de Mídia

Este projeto utiliza **Python**, **CrewAI** e integração com APIs públicas para criar uma sequência de agentes inteligentes que recomendam uma **obra literária**, uma **música**, um **filme**, uma **descrição semântica** e um **anime**, todos relacionados com o mesmo tema central.

## 🤖 Ferramentas e Agentes

### 🔧 Tools Implementadas
- **FetchLivroTool**: Recomenda um livro de um gênero aleatório entre suspense, romance, fantasia, mistério, filosofia ou autoajuda, usando a **Google Books API**.
- **FetchMusicTool**: Sugere músicas populares ou relacionadas com o gênero do livro via **Vagalume API**.
- **FetchCinefiloTool**: Indica um filme relacionado ao tema do livro, utilizando a **Simkl API**.
- **FetchDicionarioTool**: Retorna a definição do gênero usando a **DictionaryAPI.dev**.
- **FetchOtakuTool**: Sugere um anime com base no mesmo tema através da **AniAPI**.

### 🧠 Lógica dos Agentes
1. O primeiro agente escolhe o livro e define o tema.
2. Os demais agentes fazem recomendações com base nesse tema.
3. O resultado final é um pacote completo de mídia com:
   - 📕 Livro
   - 🎶 Música
   - 🎬 Filme
   - 🧠 Significado
   - 🎌 Anime

## 🧪 Tecnologias Utilizadas

- Python
- CrewAI
- requests
- APIs Públicas (Google Books, Vagalume, Simkl, DictionaryAPI, AniAPI)

---

## 📘 Objetivo Acadêmico

Este projeto foi desenvolvido como parte de um **trabalho para a disciplina de Inteligência Artificial Generativa** da faculdade, com foco em **integração de LLMs e APIs externas**.

---

> Desenvolvido com dedicação por **João Gabriel Santos** – @JonGMS