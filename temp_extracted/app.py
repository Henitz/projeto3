import streamlit as st
import os
import zipfile

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
st.title("Aplicação Streamlit")

# Diretório temporário para extração
temp_dir = "temp_extracted"

# Verifica se o diretório temporário existe, senão, cria
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Caminho do arquivo ZIP
zip_path = "data/arquivo.zip"

# Verifica se o arquivo ZIP existe
if os.path.exists(zip_path):
    try:
        # Limpa o diretório temporário antes da extração
        clean_temp_dir(temp_dir)

        # Extrai os arquivos do ZIP para o diretório temporário
        extract_zip(zip_path, temp_dir)

        st.success("Arquivo ZIP extraído com sucesso!")

        # Aqui você pode continuar o código para processar os arquivos extraídos
        # ...

    except Exception as e:
        st.error(f"Erro ao extrair o arquivo ZIP: {e}")

else:
    st.warning("O arquivo ZIP não foi encontrado. Verifique o caminho.")

# Notas adicionais:
# Certifique-se de substituir "caminho/do/seu/arquivo.zip" pelo caminho real do seu arquivo ZIP.
# Adicione o restante do código para processar os arquivos extraídos conforme necessário.
