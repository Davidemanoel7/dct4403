import random
import sys
import time

from paho.mqtt import client as mqtt_client


host = '127.0.0.1'
port = 1883
topic = "calc/op"

client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect( client, userdata, flags, rc, properties ):
        if rc == 0:
            print("Connected to MQTT Broker!\n")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(
        callback_api_version= mqtt_client.CallbackAPIVersion.VERSION2,
        client_id=client_id )
    client.on_connect = on_connect
    client.connect( host=host, port=port, keepalive=60 )
    return client


def publish( client ):
    while True:
        time.sleep(1)

        msg = f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]}"
        print(msg)
        
        result = client.publish( topic, msg )

        status = result[0]

        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        run()
    else:
        print("<op> is ADD, SUB, MUL, DIV math operations to numbers a and b\n")
        print("Type: <op> a b")
        print("Example: SUM 1 2")
