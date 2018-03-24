import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Broker...")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("===>>> Connection FAILED!")

def on_message(client, userdata, message):
    msgSub = str(message.payload)[2:30]
    print("Message received: <"+msgSub+">")

Connected = False   #global variable for the state of the connection

brokerAddr = "m10.cloudmqtt.com"  #Broker address
port = 16826                      #Broker port
usr = "ejdvexlm"                  #Connection username
pwd = "R4RudWoYQdP2"              #Connection password

client = mqttClient.Client("pyApp")          #create new instance
client.username_pw_set(usr, password=pwd)    #set username and password
client.on_connect= on_connect                #attach function to callback
client.on_message= on_message                #attach function to callback

client.connect(brokerAddr, port=port)    #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("dataLogger")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\n Script aborted...")
    client.disconnect()
    client.loop_stop()
