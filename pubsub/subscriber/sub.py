import random
import signal
from paho.mqtt import client as mqtt_client

host = '127.0.0.1'
port = 1883
topic = "calc/op"
client_id = f'python-mqtt-{random.randint(0, 100)}'

# signal = signal.signal( signal.SIGINT, quit )


def connect_mqtt() -> mqtt_client:
    def on_connect( client, userdata, flags, rc, properties ):
        if rc == 0:
            print(f"Connected to MQTT {host}!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(
        callback_api_version= mqtt_client.CallbackAPIVersion.VERSION2,
        client_id=client_id )
    
    client.on_connect = on_connect
    client.connect( host=host, port=port, keepalive=60 )
    
    return client


def subscribe( client: mqtt_client ):
    client.subscribe(topic)
    client.on_message = on_message

def on_message( client, userdata, msg ):
        # msg = msg.payload.decode()
        print(f"Easy: {msg.payload}")

        # op = msg[0]

        # match op:
        #     case 'ADD':
        #         print(add( 1, 1 ))
        #         return
        #     case 'SUB':
        #         print(sub( 1, 1 ))
        #         return
        #     case 'MUL':
        #         print(mul( 1, 1))
        #         return
        #     case 'DIV':
        #         print(div( 1, 1 ))
        #         return
        #     case __:
        #         return


def on_disconnect(client, userdata, flags, rc, properties):
    print("Disconnected successfully.")


def run():
    client = connect_mqtt()
    subscribe(client)

    client.on_disconnect = on_disconnect

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