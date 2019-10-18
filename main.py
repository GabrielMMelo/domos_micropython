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

ID_DEVICE = 1  # device's identifier

websocket = False
token = None
id_device = None

int_pin = Pin(INT_PIN, Pin.IN, Pin.PULL_UP)
output_pin = Pin(OUTPUT_PIN, Pin.OUT) 

# TODO:
# 1º realizar login e guardar o token
# 2º Enviar requisicao no endpoint da api para criar o device, se nao existir
# 3º receber resposta da api com o id do device atual

def login():
    global token

    url = 'http://' + settings["HOST"] + '/api/v1/auth/login/'
    data = {
        "username": settings["USERNAME"],
        "password": settings["PASSWD"]
    }
    headers = {
        "content-type": 'application/json'
    }
    r = requests.post(url=url, headers=headers, json=data)
    token = r.json()["key"]



def connect_ws():
    global websocket

    websocket = False
    while not websocket:
        try:
            websocket = uwebsockets.client.connect(
                'ws://' + settings['HOST'] + '/ws/device/{}/'.format(ID_DEVICE)
            )

            message = {
                'state': output_pin.value(),
                'token': "f6a981aa1a7fd050454afd5f4d4a030f20b6152c"
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

login()
print("TOKEN", token)
connect_ws()
wait_4_messages()
