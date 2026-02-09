from google.cloud import pubsub_v1
import json

# Definir seu Project ID (você vai mudar isso)
PROJECT_ID = "hello-4ch-93603-486512"
TOPIC_ID = "hello-4ch-topic"

# Criar o publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

# Mensagem que será publicada
message = {
    "mensagem": "Ola do 4CH!",
    "timestamp": "2025-02-09"
}

# Converter para JSON
message_json = json.dumps(message).encode("utf-8")

# Publicar a mensagem
future = publisher.publish(topic_path, data=message_json)
message_id = future.result()

print(f"Mensagem publicada com ID: {message_id}")

#18422422859774081