import streamlit as st
import json
import os
import webbrowser

text_path = os.path.join('assets', 'textos', 'main.json')

# Carregar os dados do arquivo JSON
with open(text_path, 'r', encoding='utf-8') as f:
    dados = json.load(f)

def estoque():

    st.title("Bem-vindo ao Stocky")

    # Exibir a imagem principal
    imagem_path = "assets/images/logo_sem_fundo_texto"
    st.image(imagem_path, width=400)

    # Exibir mensagem inicial
    st.write(dados['mensagem_inicial'])
    st.markdown("---")



