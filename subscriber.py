from google.cloud import pubsub_v1
import time

PROJECT_ID = "hello-4ch-93603-486512"
SUBSCRIPTION_ID = "hello-4ch-subscription"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

def callback(message):
    print(f"Mensagem recebida: {message.data.decode('utf-8')}")
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

print("Aguardando mensagens... (pressione Ctrl+C para sair)")
try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()
    print("Encerrando...")

    