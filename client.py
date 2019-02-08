from machine import Pin 
import os
import uwebsockets.client


class NodeWebSocket():
    def __init__(self):
        self.uri = "ws://192.168.0.110:8000/ws/node/node_1/" 
        self.response = ''
        self.trigger = Pin(18, Pin.IN, Pin.PULL_UP)
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
