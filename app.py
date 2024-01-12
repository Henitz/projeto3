import streamlit as st
import os
import zipfile
import shutil

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

# Mensagem para o usuário fornecer o caminho do arquivo ZIP
zip_path = st.text_input("Digite o caminho do arquivo ZIP:")

if st.button("Executar"):
    try:
        # Limpa o diretório temporário antes da extração
        clean_temp_dir(temp_dir)

        # Extrai os arquivos do ZIP para o diretório temporário
        extract_zip(zip_path, temp_dir)

        st.success("Arquivo ZIP extraído com sucesso!")

        # Executando o arquivo projeto.py
        projeto_path = os.path.join(temp_dir, "projeto.py")
        st.write(f"Executando {projeto_path}")
        os.system(f"streamlit run {projeto_path}")

    except Exception as e:
        st.error(f"Erro ao extrair o arquivo ZIP: {e}")
