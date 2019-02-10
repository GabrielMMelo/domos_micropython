from machine import Pin 
import os
import uwebsockets.client

import settings


class NodeWebSocket():
    def __init__(self):
        self.uri = "ws://{}:{}/ws/node/node_{}/".format(
                settings.SERVER_HOST,
                settings.SERVER_PORT,
                settings.NODE_ID)
         
        self.response = ''
        self.trigger = Pin(settings.DEVICES[0], Pin.IN, Pin.PULL_UP)
        self.trigger.irq(trigger=Pin.IRQ_FALLING, handler=self.sender)
        self.listener()

    def sender(self, trigger):
        message = '{"message": "' + str(self.trigger.value()) + '"}'  
        self.ws.send(message)
        print("mensagem enviada")

    def listener(self):
        self.ws = uwebsockets.client.connect(self.uri)
        while True:
            self.response = self.ws.recv()
            print(self.response)


nodews = NodeWebSocket()
