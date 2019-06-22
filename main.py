import gc
import json

from machine import Pin
import uwebsockets.client

from mac import get_mac

ID_DEVICE = 1
WORK_PIN = 18

try:
    f = open('mac')
    mac = f.read()
    print("mac", mac)
    f.close()
except OSError:
    mac = None

websocket = False
while not websocket:
    try:
        websocket = uwebsockets.client.connect(
            'ws://192.168.0.110:8000/ws/device/{}/'.format(ID_DEVICE))
    except OSError:
        websocket = False

# TODO: timer interrupt to send periodic updates to server

if mac is None:
    mac = get_mac()
    print("mac novo:", mac)
    message = {'mac': mac}
    websocket.send(json.dumps(message))


# Interrupt handler
def toggle_mode(toggler):
    print(toggler.value())
    message = {'state': str(toggler.value())}
    websocket.send(json.dumps(message))


work_pin = Pin(WORK_PIN, Pin.IN, Pin.PULL_UP)
work_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=toggle_mode)


def wait_4_messages():
    while True:
        message = websocket.recv()
        try:
            state = json.loads(message)['state']
        except TypeError:  # needed to avoid None return while interrupt handler is working
            state = work_pin.value()
        print("Message:", state)
        work_pin.value(state)


wait_4_messages()
