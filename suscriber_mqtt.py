import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
# ---------------------------------------------------------------
broker_address = "localhost"
topic = "test/topic"
client = mqtt.Client("Suscriber")
# ---------------------------------------------------------------
def on_message(client, userdata, message):
    decoded_message = message.payload.decode("utf-8")
    print(f"Message received: '{decoded_message}")
# -------------------------------------------------------------------
try:
    c = client.connect(broker_address)
    # print(f"Connection Succeded {c}")
    client.on_message = on_message
except Exception as e:
    print(f"Error {e}")
# ---------------------------------------------------------------
if not c:
    client.subscribe(topic, qos=1)
    client.loop_forever()
else:
    print("Suscriber Status:    Disconnected")
# ---------------------------------------------------------------
# message = subscribe.callback(on_message,topics = topic,
#                                  hostname = broker_address,
#                                  port = 1883, keepalive = 60)

