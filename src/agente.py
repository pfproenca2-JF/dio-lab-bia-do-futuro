import pandas as pd
import json
import google.generativeai as genai
from config import Config

class IAGOGerente:
    def __init__(self):
        # Configura a IA
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-pro')
        
    def ler_dados(self):
        # Carrega a base de conhecimento (Knowledge Base)
        transacoes = pd.read_csv(Config.TRANSACOES_FILE)
        with open(Config.PERFIL_FILE, 'r') as f:
            perfil = json.load(f)
        return transacoes, perfil

    def gerar_resposta(self, user_input):
        transacoes, perfil = self.ler_dados()
        
        # Monta o contexto para o RAG (Retrieval Augmented Generation)
        contexto = f"""
        Você é o IAGO, Gerente Operacional Financeiro.
        Dados do Cliente: {perfil}
        Resumo de Transações: {transacoes.tail(5).to_dict()}
        
        Instrução: Responda de forma técnica e proativa.
        """
        
        prompt_completo = f"{contexto}\nUsuário: {user_input}"
        
        try:
            response = self.model.generate_content(prompt_completo)
            return response.text
        except Exception as e:
            return f"IAGO Error: Erro operacional ao conectar com a IA. {str(e)}"
          
