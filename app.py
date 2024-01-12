import streamlit as st
import os
import zipfile
import shutil

# Diretório temporário para extração
temp_dir = "temp_extracted"

# Verifica se o diretório temporário existe, senão, cria
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
else:
    st.warning("O diretório temporário já existe. Tentando removê-lo.")

    # Tentar remover o diretório temporário
    try:
        shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
    except Exception as e:
        st.error(f"Erro ao tentar remover o diretório temporário: {e}")

# Obtém o caminho absoluto do diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho para o arquivo ZIP
zip_path = os.path.join(script_dir, 'data', 'app.zip')

# Verifica se o arquivo ZIP existe
if os.path.exists(zip_path):
    try:
        # Limpa o diretório temporário antes da extração
        shutil.rmtree(temp_dir, ignore_errors=True)

        # Extrai os arquivos do ZIP para o diretório temporário
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        st.success("Arquivo ZIP extraído com sucesso!")

        # Executando o arquivo projeto.py
        projeto_path = os.path.join(temp_dir, "projeto.py")
        st.write(f"Executando {projeto_path}")
        os.system(f"streamlit run {projeto_path}")

    except Exception as e:
        st.error(f"Erro ao extrair o arquivo ZIP: {e}")

else:
    st.warning("O arquivo ZIP não foi encontrado. Verifique o caminho.")
