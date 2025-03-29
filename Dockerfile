# Usa a imagem oficial do Python
FROM python:3.11

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pelo Django
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
