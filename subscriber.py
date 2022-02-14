#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Subscriber

# Connecting with the broker by the topic mqtt/printer
def on_connect(client, userdata, flags, rc):
    print("Connected ....")
    client.subscribe("mqtt/printer")

def on_message(client, userdata, msg):
     # Receiving the message and convert it to uppercase
     print("Received message: ", str(msg.payload.decode("utf-8").upper()))


# create a subscriber and se the same port and the same host
client = mqtt.Client()
if client.connect("localhost",1883) != 0 :
    print("We can not connect to the MQTT broker!")
    sys.exit(-1)

client.on_connect = on_connect
client.on_message = on_message

try :
    print("Press Ctl+C tp exit ...")
    client.loop_forever()
except :
    print("Disconnecting ....")
    client.disconnect()
