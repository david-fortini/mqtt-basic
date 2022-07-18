#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Publisher
# '192.168.1.101' mac
client = mqtt.Client()
endpoint = '192.168.1.107' # 127.0.0.1 # localhost # 192.168.1.106
endpoint='192.168.178.175'
client.connect(endpoint,1883,60)
client.publish("topic/test", "Hello world from linux");
client.disconnect();
print('finished succesfully')