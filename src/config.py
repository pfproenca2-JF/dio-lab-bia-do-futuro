import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    # Caminhos dos dados
    DATA_PATH = "../data/"
    TRANSACOES_FILE = f"{DATA_PATH}transacoes.csv"
    PERFIL_FILE = f"{DATA_PATH}perfil_investidor.json"
    PRODUTOS_FILE = f"{DATA_PATH}produtos_financeiros.json"
  
