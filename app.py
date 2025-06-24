import streamlit as st

st.title("Cadastro de Clientes")

nome = st.text_input("Digite o nome do cliente:")
idade = st.number_input("Digite a idade do cliente:", min_value=0, max_value=120, step=1 )
celular = st.text_input("Digite o celular do cliente:")
email = st.text_input("Digite o email do cliente:")
dt_nasc = st.date_input("Escolha a data de nascimento:")
tipo_cliente = st.selectbox("Selecione o tipo de cliente:", ["Pessoa Física", "Pessoa Jurídica"]) 

cadastrar = st.button("Cadastrar Cliente")

if cadastrar:
    with open("clientes.csv", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Idade: {idade}\n")
        arquivo.write(f"Endereço: {email}\n")
        arquivo.write(f"Celular: {celular}\n")
        arquivo.write(f"Data de Nascimento: {dt_nasc}\n")
        arquivo.write(f"Tipo de Cliente: {tipo_cliente}\n")
        arquivo.write("\n")
        st.success("Cliente cadastrado com sucesso!")