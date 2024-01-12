import streamlit as st
import os
import zipfile
import shutil
import time  # Importe o módulo time

# Limpeza do diretório temporário antes de extrair o ZIP
shutil.rmtree("temp_extracted", ignore_errors=True)


# Função para extrair arquivos ZIP
def extract_zip(zip_path, temp_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)


# Função para limpar o diretório temporário
def clean_temp_dir(temp_dir):
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)


# Configuração do Streamlit
st.title("Aplicativo Streamlit para Processar Arquivo .zip")

# Diretório temporário para extração
temp_dir = "temp_extracted"

# Verifica se o diretório temporário existe, senão, cria
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Obtém o caminho absoluto do diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho para o arquivo ZIP
zip_path = os.path.join(script_dir, 'data', 'app.zip')

# Verifica se o arquivo ZIP existe
if os.path.exists(zip_path):
    try:
        # Limpa o diretório temporário antes da extração
        clean_temp_dir(temp_dir)

        # Extrai os arquivos do ZIP para o diretório temporário
        extract_zip(zip_path, temp_dir)

        st.success("Arquivo ZIP extraído com sucesso!")

        # Aguarde um segundo antes de executar o script Streamlit
        time.sleep(1)

        # Executando o arquivo projeto.py
        projeto_path = os.path.join(temp_dir, "projeto.py")
        st.write(f"Executando {projeto_path}")
        os.system(f"streamlit run {projeto_path}")

    except Exception as e:
        st.error(f"Erro ao extrair o arquivo ZIP: {e}")

else:
    st.warning("O arquivo ZIP não foi encontrado. Verifique o caminho.")
