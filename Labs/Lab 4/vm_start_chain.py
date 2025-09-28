#Team members: Vardhan Jain, Shaurya Goel
#Github repo link: https://github.com/2shaurya4/ee250

# vm_start_chain.py
import os, time
import paho.mqtt.client as mqtt

BROKER = os.environ.get("BROKER", "localhost")   # set to RPI_IP from VM, e.g. "192.168.1.42"
PORT = int(os.environ.get("BROKER_PORT", 1883))
USER = os.environ.get("USERNAME", "USERNAME")

client = mqtt.Client(client_id=f"start_chain_{os.getpid()}")

def on_connect(c, userdata, flags, rc):
    print("Connected to broker, subscribing to", f"{USER}/pong")
    c.subscribe(f"{USER}/pong")

def on_pong(c, userdata, message):
    try:
        n = int(message.payload.decode())
    except Exception:
        print("Received non-int pong:", message.payload)
        return
    print("[start] Received pong:", n)
    new = n + 1
    print("[start] Publishing ping:", new)
    time.sleep(1)    # prevent race too fast
    c.publish(f"{USER}/ping", payload=str(new))

client.on_connect = on_connect
client.message_callback_add(f"{USER}/pong", on_pong)

client.connect(BROKER, PORT, 60)
client.loop_start()

# publish initial ping to start the chain
initial = int(os.environ.get("START_VAL", "0"))
print("Publishing initial ping:", initial)
client.publish(f"{USER}/ping", payload=str(initial))

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    client.loop_stop()
    client.disconnect()
