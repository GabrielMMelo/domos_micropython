import gc
import json
import urequests as requests
from machine import Pin

import uwebsockets.client

from constants import (
    OUTPUT_PIN,
    INT_PIN,
    MAC_ADDRESS,
)

from settings import write_settings, read_settings

'''
test = {
    "HOST": "gabrielmelo.ddns.net:8081",
    "SSID": "zezinho",
    "PASSWD_NET": "JoseAnjo43",
    "USERNAME": "admin",
    "PASSWD": "@admin03OTM",
}

write_settings(test)
'''

settings = read_settings()
print("SETTINGS", settings)

websocket = False
token = None
device_id = None

int_pin = Pin(INT_PIN, Pin.IN, Pin.PULL_UP)
output_pin = Pin(OUTPUT_PIN, Pin.OUT) 

def login():
    """ Log in through the REST api and get the valid token """
    global token

    url = 'http://' + settings["HOST"] + '/api/v1/auth/login/'
    data = {
        "username": settings["USERNAME"],
        "password": settings["PASSWD"]
    }
    headers = {
        "content-type": 'application/json'
    }
    try:
        r = requests.post(url=url, headers=headers, json=data)
    except Exception as e:
        # print(e)
        return False
    token = r.json()["key"]
    return True

def get_device_id():
    """ 
    Get the device id from the given user (token) and mac address from the REST api.
    If the device doesnt exists, it will be created and its id returned too.
    """
    global device_id
    global token

    url = 'http://' + settings["HOST"] + '/api/v1/device/'
    data = {
        "mac": MAC_ADDRESS,
        "name": settings.get("DVC_NAME", 'Generic')
    }

    headers = {
        "content-type": 'application/json',
        "Authorization": 'Token ' + token
    }

    try:
        r = requests.post(url=url, headers=headers, json=data)
    except Exception as e:
        # print(e)
        return False
    device_id = r.json()["id"]
    return True


def connect_ws():
    global websocket
    global device_id
    global token

    websocket = False
    while not websocket:
        try:
            websocket = uwebsockets.client.connect(
                'ws://' + settings['HOST'] + '/ws/device/{}/'.format(device_id)
            )

            message = {
                'state': output_pin.value(),
                'token': token
            }

            websocket.send(json.dumps(message))  # send message when connect to be authenticated
        except OSError:
            websocket = False


def toggle_state(toggler):
    if toggler.value() != output_pin.value():

        print("Interruption! Pin value:", toggler.value())
        output_pin.value(toggler.value())

        message = {
            'state': output_pin.value()
        }

        try:
            websocket.send(json.dumps(message))
        except Exception as e:
            print("ERROR", e)


def wait_4_messages():
    while True:
        try:
            message = websocket.recv()
        except AssertionError:
            connect_ws()
        try:
            state = int(json.loads(message)['state'])
            if state != int(output_pin.value()):
                print("Message (from ws):", state)
                print("Pin value:", output_pin.value())
                output_pin.value(state)
        except TypeError:  # needed to avoid None return while interrupt handler is working
            pass


int_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=toggle_state)

while not login():
    pass
print("TOKEN", token)
while not get_device_id():
    pass
print("Device id", device_id)
connect_ws()
wait_4_messages()
