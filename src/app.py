import streamlit as st
from agente import IAGOGerente

# 1. Configuração Visual da Interface
st.set_page_config(page_title="IAGO - Gerente Operacional", page_icon="🤖")

# 2. Inicialização do Agente (Mantém o IAGO vivo durante a sessão)
if "agente" not in st.session_state:
    st.session_state.agente = IAGOGerente()

st.title("🤖 IAGO")
st.subheader("Inteligência Artificial Gerente Operacional")

# 3. Histórico de Mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Campo de Entrada do Usuário
if prompt := st.chat_input("Como posso ajudar sua operação financeira hoje?"):
    # Adiciona pergunta do usuário ao chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 5. Resposta do IAGO
    with st.chat_message("assistant"):
        # O app.py chama o método que criamos no agente.py
        response = st.session_state.agente.gerar_resposta(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        
