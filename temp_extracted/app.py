import streamlit as st
import zipfile
import os

st.title("Aplicativo Streamlit para Processar Arquivo .zip")

# Carregar o arquivo .zip
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

    model_file_path = "model.py"

    # Verificar se o arquivo model.py está presente no diretório
    if os.path.isfile(model_file_path):
        try:
            # Tente importar o arquivo model.py
            import model

            print("Arquivo model.py encontrado e importado com sucesso!")
        except ImportError as e:
            print(f"Erro ao importar model.py: {e}")
    else:
        print(f"Arquivo model.py não encontrado no diretório.")

    # Executando o arquivo projeto.py
    projeto_path = os.path.join(temp_dir, "projeto.py")
    st.write(f"Executando {projeto_path}")
    os.system(f"streamlit run {projeto_path}")
