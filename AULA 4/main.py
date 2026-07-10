# Título
# Input do chat
# A cada mensagem enviada:
    # Mostrar a mensagem que o usuário enviou no chat
    # Enviar essa mensagem para a IA responder
    # Aparece na tela a resposta da IA

# streamlit - frontend e backend

# pyrefly: ignore [missing-import]
import streamlit as st
# pyrefly: ignore [missing-import]
from openai import OpenAI

modelo = OpenAI(api_key="[ENCRYPTION_KEY]")

st.write("## ChatBot com IA")

# Session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# Adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# Exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # User -> Ser humano
    # Assistant -> Inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # Resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content

    # Exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)