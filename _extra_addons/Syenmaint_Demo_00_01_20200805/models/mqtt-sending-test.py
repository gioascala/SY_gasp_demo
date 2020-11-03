#!/usr/bin/env python3

import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("192.168.43.74",1883,60)
# per resettare il contatore della spellafili
client.publish("inTopic", "Reset_spell");
client.disconnect();