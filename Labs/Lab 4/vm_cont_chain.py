#Team members: Vardhan Jain, Shaurya Goel
#Github repo link: https://github.com/2shaurya4/ee250

# vm_cont_chain.py
import os, time
import paho.mqtt.client as mqtt

BROKER = os.environ.get("BROKER", "localhost")
PORT = int(os.environ.get("BROKER_PORT", 1883))
USER = os.environ.get("USERNAME", "USERNAME")

client = mqtt.Client(client_id=f"cont_chain_{os.getpid()}")

def on_connect(c, userdata, flags, rc):
    print("Connected, subscribing to", f"{USER}/ping")
    c.subscribe(f"{USER}/ping")

def on_ping(c, userdata, message):
    try:
        m = int(message.payload.decode())
    except Exception:
        print("Received non-int ping:", message.payload)
        return
    print("[cont] Received ping:", m)
    new = m + 1
    print("[cont] Publishing pong:", new)
    time.sleep(1)
    c.publish(f"{USER}/pong", payload=str(new))

client.on_connect = on_connect
client.message_callback_add(f"{USER}/ping", on_ping)

client.connect(BROKER, PORT, 60)
client.loop_forever()
