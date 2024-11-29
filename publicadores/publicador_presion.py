import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
port = 1883
topic = "sensor/presion"

client = mqtt.Client("Publicador_Presion")
client.connect(broker, port)

while True:
    presion = random.uniform(20.0, 30.0)
    client.publish(topic, f"Presion: {presion:.2f} °C")
    print(f"Publicado: {presion:.2f} °C en {topic}")
    time.sleep(2)