# script to subscribe to the CloudMQ Broker
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received: ", str(message.payload.decode("utf-8")))
    print("message topic: ", message.topic)
    print("message qos: ", message.qos)
    print("message retain flag: ", message.retain)

def on_log(client, userdata, level, buf):
    print("log: ", buf)
    
# main progr
broker_address = "m10.cloudmqtt.com"

print("1. Creating new instance")
client = mqtt.Client(client_id="dL1", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")

client.on_message = on_message
client.on_log = on_log

print("2. Connecting to Broker")
client.connect(broker_address, port=16826, keepalive=60, bind_address="")

client.loop_start()

print("3. Subscribing to topic: dataLogger",)
client.subscribe("dataLogger", qos=0)
