import streamlit as st
from Paciente import paciente
from datetime import datetime
st.header("Dados do paciente")

nome = st.text_input("nome:")
cpf = st.text_input("CPF:")
telefone = st.text_input("Fone:")
nascimento = st.text_input("Nascimento")

if st.button("Idade"):
    st.write(nome)
    p = paciente(cpf, telefone, nascimento)
    st.write(p)
