# Publish Subscribe

Status: In progress
Course: Software Engineering
Due date: November 29, 2024
Type: Homework

# Integrantes

- Marlon Sneyder Barajas Acelas - 2202042
- Karen Juliana Mora Jaimes - 2202027

# Video de implementación

[![Modelo Publish Subscribe - Mosquitto - Ingeniería de Software - Grupo B1](https://img.youtube.com/vi/4MyeKJ1JJis/maxresdefault.jpg)](https://youtu.be/4MyeKJ1JJis)

# Desarrollo

## Instalación de mosquitto

Paquetes y librerías

```bash
$ sudo apt update
$ sudo apt install mosquitto mosquitto-clients
$ sudo apt install npm
$ npm install mqtt
$ sudo apt install pip
$ sudo apt install python3-paho-mqtt
```

## Implementación

### Máquina A

Esta máquina está designada para implementar el broker y los publicadores con python.

```bash
$ sudo systemctl stop mosquitto #si el puerto 1883 se encuentra ocupado por una instancia anterior de mosquitto
$ mosquitto -v
```

**publicador_temperatura.py**

```python
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
```

**publicador_humedad.py**

```python
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
```

**publicador_presion.py**

```python
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
```

### Máquina B

La máquina B será destinada a contener los suscriptores, con node.js.

```bash
# instalar node.js y npm
$ npm install mqtt
```

**suscriptor_temperatura.js**

```jsx
const mqtt = require('mqtt');

const broker = 'mqtt://<ip_del_broker>';
const topic = 'sensor/temperatura';

const client = mqtt.connect(broker);

client.on('connect', () => {
    console.log(`Conectado al broker en ${broker}`);
    client.subscribe(topic, (err) => {
        if (!err) {
            console.log(`Suscrito al tema ${topic}`);
        } else {
            console.error('Error al suscribirse:', err);
        }
    });
});

client.on('message', (topic, message) => {
    console.log(`Mensaje recibido en ${topic}: ${message.toString()}`);
});
```

**suscriptor_humedad.js**

```jsx
const mqtt = require('mqtt');

const broker = 'mqtt://<ip_del_broker>';
const topic = 'sensor/humedad';

const client = mqtt.connect(broker);

client.on('connect', () => {
    console.log(`Conectado al broker en ${broker}`);
    client.subscribe(topic, (err) => {
        if (!err) {
            console.log(`Suscrito al tema ${topic}`);
        } else {
            console.error('Error al suscribirse:', err);
        }
    });
});

client.on('message', (topic, message) => {
    console.log(`Mensaje recibido en ${topic}: ${message.toString()}`);
});
```

**suscriptor_presion.js**

```jsx
const mqtt = require('mqtt');

const broker = 'mqtt://<ip_del_broker>';
const topic = 'sensor/presion';

const client = mqtt.connect(broker);

client.on('connect', () => {
    console.log(`Conectado al broker en ${broker}`);
    client.subscribe(topic, (err) => {
        if (!err) {
            console.log(`Suscrito al tema ${topic}`);
        } else {
            console.error('Error al suscribirse:', err);
        }
    });
});

client.on('message', (topic, message) => {
    console.log(`Mensaje recibido en ${topic}: ${message.toString()}`);
});
```

## Testeo

### Publicadores

```bash
$ python3 publicador_temperatura.py
$ python3 publicador_humedad.py
$ python3 publicador_presion.py
```

### Suscriptores

```bash
node **suscriptor_temperatura.js
node suscriptor_humedad.js
node suscriptor_presion.js**
```