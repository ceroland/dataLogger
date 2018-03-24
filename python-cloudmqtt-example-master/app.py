# This publishes messages to cloudmqtt.com and also subscribes to it.
# Publishes an On/OFF messages to the Cloudmqtt
# At the other end - we have the Arduino sketch which is listening to this message
# and turns on and off the LEDs.

# Good example of a full end to end solution,
# this code has to be run on a laptop, You will need a cloudmqtt account.
# at the other end you will have the Arduino sketch listening to messages and will print
# on the serial monitor

import paho.mqtt.client as mqtt
import os, urlparse, time

# Define event callbacks
def on_connect(mosq, obj, rc):
    print ("on_connect:: Connected with result code "+ str ( rc ) )
    #print("rc: " + str(rc))
    #print("")

def on_message(mosq, obj, msg):
    #print ("on_message:: this means I got a message from broker for this topic")
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print("")

def on_publish(mosq, obj, mid):
    #print("mid: " + str(mid))
    print("")

def on_subscribe(mosq, obj, mid, granted_qos):
    print("This means broker has acknowledged my subscribe request")
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)


client = mqtt.Client()
# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe

# Uncomment to enable debug messages
# client.on_log = on_log

# user name has to be called before connect - my notes.
client.username_pw_set("ejdvexlm", "R4RudWoYQdP2")

client.connect('m10.cloudmqtt.com', 16826, 60)

# Continue the network loop, exit when an error occurs
#rc = 0
#while rc == 0:
#    rc = client.loop()
#print("rc: " + str(rc))

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()

client.loop_start()

client.subscribe ("/dataLogger",0)

rc = 0
while rc == 0:
    #client.publish ( "/toclientloud", "from python code")

    rc = client.loop()

    for i in range(15):
        print(".", end="", flush=True)
        time.sleep(0.2)
    print(chr(27) + "[2J") # or print('\x1b[2J')
print("rc: ", str(rc))
