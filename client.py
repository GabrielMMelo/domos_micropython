import uwebsockets.client
import os

def hello():
    with uwebsockets.client.connect('ws://192.168.0.110:8000/ws/chat/gabriel/') as websocket:

        uname = os.uname()
        name = '{sysname} {release} {version} {machine}'.format(
            sysname=uname.sysname,
            release=uname.release,
            version=uname.version,
            machine=uname.machine,
        )
        
        name = '{"message": "' + name + '"}'
        websocket.send(name)
        print("> {}".format(name))

        greeting = websocket.recv()
        print("< {}".format(greeting))

hello()
