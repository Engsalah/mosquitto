#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# create a publisher
client = mqtt.Client()

# we set the host address or we can set the IP
# the default port is 1883
if client.connect("localhost",1883) != 0 :
    print("We can not connect to the MQTT broker")
    sys.exit(-1)


msg = input("Write your message to the subscriber/s : ")
#msg = msg.upper()

# set the topic name and send the message
client.publish("mqtt/printer", msg)

