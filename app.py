import streamlit as st
import zipfile
import os

st.title("Aplicativo Streamlit para Processar Arquivo .zip")

# Caminho relativo para o arquivo ZIP no diretório "data"
zip_file_path = os.path.join("data", "app.zip")

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extraindo o conteúdo para um diretório temporário
    temp_dir = "temp_extracted"
    zip_ref.extractall(temp_dir)

    # Listando os arquivos extraídos
    extracted_files = os.listdir(temp_dir)

# Exibindo a lista de arquivos extraídos
st.write("Arquivos extraídos:")
for file in extracted_files:
    st.write(file)
