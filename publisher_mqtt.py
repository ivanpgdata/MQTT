import paho.mqtt.client as mqtt
import numpy as np
import time
# ---------------------------------------------------------------
broker_address = "localhost"
topic = "test/topic"
client = mqtt.Client("Publisher")
# ---------------------------------------------------------------
try:
    c = client.connect(broker_address)
    # print(f"Connection Succeded {c}")
except Exception as e:
    print(f"Error {e}")
# ---------------------------------------------------------------
if not c :
    while True:
        n = np.random.rand()
        t = 3
        time.sleep(t)
        message = f"Hello Github, this is the Publisher's message with the random number {n}." \
                  f" As you can see this message is sent every {t} seconds"
        c = client.publish(topic, message)
        print(message)
else:
    print("Publisher Status:   Disconnected")
# ---------------------------------------------------------------
client.disconnect()
# ---------------------------------------------------------------
# image_and_ports = docker run -it -p 1883:1883 -p 9001:9001 eclipse-mosquitto:1.4.8