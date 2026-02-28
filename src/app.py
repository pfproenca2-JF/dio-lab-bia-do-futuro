import streamlit as st
import pandas as pd
import json
import os
from dotenv import load_dotenv

# Configuração da página
st.set_page_config(page_title="IAGO - Gerente Operacional", page_icon="🤖")

def carregar_contexto():
    # Carrega os dados simulando a base de conhecimento do IAGO
    transacoes = pd.read_csv('../data/transacoes.csv')
    with open('../data/perfil_investidor.json', 'r') as f:
        perfil = json.load(f)
    with open('../data/produtos_financeiros.json', 'r') as f:
        produtos = json.load(f)
    return transacoes, perfil, produtos

st.title("🤖 IAGO")
st.subheader("Inteligência Artificial Gerente Operacional")

# Sidebar com resumo do perfil
transacoes, perfil, produtos = carregar_contexto()
st.sidebar.header("Perfil do Cliente")
st.sidebar.write(f"**Nome:** {perfil.get('nome', 'Cliente')}")
st.sidebar.write(f"**Perfil:** {perfil.get('perfil', 'Não definido')}")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Como posso ajudar sua operação financeira hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Lógica Simulada do IAGO (Enquanto você não configura a chave da API)
        if "gastos" in prompt.lower():
            total = transacoes['valor'].sum()
            response = f"IAGO informa: Analisando o arquivo `transacoes.csv`, seu gasto total acumulado é de R$ {total:.2f}."
        elif "investir" in prompt.lower():
            response = f"Com base no seu perfil **{perfil['perfil']}**, recomendo olhar os produtos no arquivo `produtos_financeiros.json`."
        else:
            response = "Sou o IAGO, seu Gerente Operacional. Posso analisar seus gastos ou sugerir investimentos baseados nos seus dados."
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
      
