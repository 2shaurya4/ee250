#Team members: Vardhan Jain, Shaurya Goel
#Github repo link: https://github.com/2shaurya4/ee250


"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))


if __name__ == '__main__':
    #get IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname) 
    #username = "vrjain"
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python.
        
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1)

    while True:
        #replace user with your USC username in all subscriptions
        client.publish("vrjain/ipinfo", ip_address)
        print("Publishing IP address: " + ip_address)
        time.sleep(4)

        #get date and time 
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        #publish date and time in their own topics
        client.publish("vrjain/date", date_str)
        print("Publishing Date: " + date_str)
        time.sleep(2)
        
        client.publish("vrjain/time", time_str)
        print("Publishing Time: " + time_str)
        time.sleep(2)
