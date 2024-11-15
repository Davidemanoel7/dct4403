import random
# import signal
from paho.mqtt import client as mqtt_client

host = '127.0.0.53'
port = 8080
topic = "calc/op/"
client_id = f'python-mqtt-{random.randint(0, 100)}'

message_queue = {
    "last_message": "",
    "index": -1
}

# signal = signal.signal( signal.SIGINT, quit )


def connect_mqtt() -> mqtt_client:
    def on_connect( client, userdata, flags, rc, properties ):
        if rc == 0:
            print(f"Connected to MQTT {host}!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client( callback_api_version= mqtt_client.CallbackAPIVersion.VERSION2 )
    
    client.on_connect = on_connect
    client.connect( host=host, port=port, keepalive=60 )
    
    return client


def subscribe( client: mqtt_client ):
    client.subscribe( topic )
    client.on_message = on_message

def on_message( client: mqtt_client, userdata, msg ):
        decoded_msg = msg.payload.decode()
        # print(f"Receiv message: {msg}")
        
        ind = int(message_queue.get("index") + 1)

        message_queue.update( {"last_message": f"{ decoded_msg }"} )
        message_queue.update( {"index": ind } )

        # print( message_queue )

        split_msg = decoded_msg.split(" ")

        op = split_msg[0]
        a = split_msg[1]
        b = split_msg[2]

        match op:
            case 'ADD':
                print(add( a, b ))
                return
            case 'SUB':
                print(sub( a, b ))
                return
            case 'MUL':
                print(mul( a, b ))
                return
            case 'DIV':
                print(div( a, b ))
                return
            case __:
                return



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