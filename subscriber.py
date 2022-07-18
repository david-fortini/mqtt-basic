#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("#")

def on_message(client, userdata, msg):
    print('arrived message: \n')
    print(type((msg.topic)))
    print(f"topic={msg.topic}")
    print(f"payload={msg.payload.decode()}")
    #client.disconnect()


def get_local_ip() -> str:
    import socket
    
    local_ip = (([ip for ip 
                  in socket.gethostbyname_ex(socket.gethostname())[2] 
                  if not ip.startswith("127.")] or
                    [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())
                      for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
    print(f'{local_ip=}')
    return local_ip
  
local_ip = get_local_ip()
client = mqtt.Client()
ip_address = local_ip #'192.168.178.175'#'192.168.1.107' #'localhost'
client.connect(ip_address,1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()