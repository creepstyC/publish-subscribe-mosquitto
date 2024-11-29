import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
port = 1883
topic = "sensor/temperatura"

client = mqtt.Client("Publicador_Temperatura")
client.connect(broker, port)

while True:
    temperatura = random.uniform(20.0, 30.0)
    client.publish(topic, f"Temperatura: {temperatura:.2f} °C")
    print(f"Publicado: {temperatura:.2f} °C en {topic}")
    time.sleep(2)