import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
port = 1883
topic = "sensor/humedad"

client = mqtt.Client("Publicador_humedad")
client.connect(broker, port)

while True:
    humedad = random.uniform(20.0, 30.0)
    client.publish(topic, f"Humedad: {humedad:.2f} °C")
    print(f"Publicado: {humedad:.2f} °C en {topic}")
    time.sleep(2)