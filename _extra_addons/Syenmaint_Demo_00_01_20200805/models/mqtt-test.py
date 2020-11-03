#!/usr/bin/env python3

import paho.mqtt.client as mqtt


# per la connessione al topic
def on_connect(client, userdata, flags, rc):
    print("Connesso con il seguente codice " + str(rc))
    client.subscribe("CRC02/log")


def on_message(client, userdata, msg):
    print(msg.payload.decode())

# connessione al client
client = mqtt.Client()
client.connect("192.168.43.74", 1883, 60)

# associazione funzioni - eventi
client.on_connect = on_connect
client.on_message = on_message

#loop 
client.loop_forever()