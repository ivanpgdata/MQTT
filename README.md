# MQTT BROKER PROJECT: Publisher/Subscriber

This project implements an MQTT Publisher and Subscriber using Python and the `paho-mqtt` library, deployed with Docker utilizing the `eclipse-mosquitto:1.4.8` image as the MQTT broker. The Publisher sends messages to a specified topic, while the Subscriber listens and processes these messages. The project demonstrates effective communication between devices or applications using the MQTT protocol.

The project consists of:
- **Using Docker** with the image needed running.
- **Two Python Scripts**:
  - **⬆️ Publisher**: Publishes a message to a specified MQTT topic.
  - **️⬇️ Subscriber**: Subscribes to the same MQTT topic and receives the published message.
    
![](media/mqtt_pic1.jpg)

We had some issues during the project as the newest version of eclipse-mosquitto made it difficult to the subscriber to get the message, so I decided to use the 1.4.8 version instead

I had so much fun exploring this protocol and learning how it works as well as how to modify the scripts so a subscriber can also be a publisher. The posibilities are limitless, once you have this you can store the data and operate with it, or send it somewhere to create valuable information. So fun!🎉
