import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Configurações iniciais
load_dotenv()

# Configuração do LLM
def get_llm():
    return ChatGroq(
        model="groq/llama-3.3-70b-versatile",
        #model="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",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.6  # 0 a 1
    )