import os
# import paho.mqtt.client as mqtt
from django.conf import settings
import ssl



def on_connect(client, userdata, flags, reason_code,properties):

    if reason_code==0:
        print('Connected successfully on hive')
        # client.subscribe('machine_data_dev')

    else:
        print(f"Connection failed with reason code {reason_code}. Attempting to reconnect...")
        client.reconnect()


def on_message(client, userdata, msg):
    connected_machine_data = msg.payload.decode()
    topic = msg.topic

    if topic == "test":
        pass
        # all_topics(connected_machine_data,topic) want to store in database
        # from . import io_status_websocket

        # io_status_websocket.io_websocket(connected_machine_data)dashboard_websocket


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
# client.on_disconnect = on_disconnect
# client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
# client.tls_set(settings.CAPATH, certfile=settings.CERTPATH, keyfile=settings.KEYPATH,
#                     cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
# client.connect(
#
#    host=settings.AWSHOST,
#    port=settings.AWSPORT,
#    keepalive=settings.MQTT_KEEPALIVE
# )
