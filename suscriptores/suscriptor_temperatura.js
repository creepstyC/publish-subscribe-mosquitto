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