import gc
import json

from machine import Pin
import uwebsockets.client

# from mac import get_mac

ID_DEVICE = 1  # device's identifier
SWITCH = [18]  # pin ports which handle physical switch changes
ACTOR = [19]  # pin ports which properly toggle the state of the peripherics
"""
try:
    f = open('mac')
    mac = f.read()
    print("mac", mac)
    f.close()
except OSError:
    mac = None
"""

websocket = False
while not websocket:
    try:
        websocket = uwebsockets.client.connect(
            'ws://192.168.0.113:8000/ws/device/{}/'.format(ID_DEVICE))
    except OSError:
        websocket = False
"""
if mac is None:
    mac = get_mac()
    print("mac novo:", mac)
    message = {'mac': mac}
    websocket.send(json.dumps(message))
"""

switches = [Pin(switch, Pin.IN, Pin.PULL_UP) for switch in SWITCH]
actors = [Pin(actor, Pin.OUT) for actor in ACTOR]


# Interrupt handlers
# TODO: make it scalable
def toggle_mode_0(toggler):  # Change de name to port specific name
    if toggler.value() != actors[0].value():
        print("Interrupção! Valor do pino:", toggler.value())
        actors[0].value(toggler.value())

        message = {'state': str(toggler.value())}
        websocket.send(json.dumps(message))


for switch in switches:
    switch.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=toggle_mode_0)
    # TODO: make it scalable


def wait_4_messages():
    while True:
        message = websocket.recv()
        try:
            state = int(json.loads(message)['state'])
            # TODO: make it scalable
            if state != int(actors[0].value()):
                print("Message (from ws):", state)
                print("Pin value:", actors[0].value())
                actors[0].value(state)
        except TypeError:  # needed to avoid None return while interrupt handler is working
            pass


wait_4_messages()
