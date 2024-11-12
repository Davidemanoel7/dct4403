import random

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "calc/op"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect( client, userdata, flags, rc, properties ):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(
        callback_api_version= mqtt_client.CallbackAPIVersion.VERSION2,
        client_id=client_id )
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message( client, userdata, msg ):

        msg = msg.payload.decode()
        print(msg)

        print(f"Easy: {msg}")

        # op = msg.payload.decode()

        # print(f"{op}")

        # match msg.payload:
        #     case '1':
        #         return

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

def add( a, b ):
    return a + b

def sub( a, b ):
    return  a - b

def mul( a, b ):
    return a * b

def div( a, b ):
    return a/b if ( b!= 0 ) else -1

if __name__ == '__main__':
    run()