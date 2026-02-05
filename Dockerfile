# Usa a imagem oficial do Python 3.9 slim
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

COPY src/requirements.txt .


# Copia o script local para o container
COPY src/main.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Comando para executar o script
CMD ["python", "main.py"]
