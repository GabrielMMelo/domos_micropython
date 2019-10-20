import gc
import json
import time
import urequests as requests
from machine import Pin

import uwebsockets.client
import picoweb

from constants import (
    OUTPUT_PIN,
    INT_PIN,
    MODE_PIN,
    MAC_ADDRESS,
)
from settings import write_settings, read_settings
from wifi import STA, AP


'''
test = {
    "HOST": "gabrielmelo.ddns.net:8081",
    "SSID": "zezinho",
    "PASSWD_NET": "JoseAnjo43",
    "USERNAME": "admin",
    "PASSWORD": "@admin03OTM",
}

write_settings(test)
'''

app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    global settings
    yield from picoweb.start_response(resp)

    yield from app.render_template(resp, "index.tpl", args=(settings,))

@app.route("/login")
def index(req, resp):
    yield from picoweb.start_response(resp)
    if req.method == "POST":
        yield from req.read_form_data()
        settings["SSID"] = req.form["ssid"]
        settings["SSID_PASSWORD"] = req.form["password"]
        write_settings(settings)

        STA.connect()
        STA.configure(settings["SSID"], settings["SSID_PASSWORD"])

        time.sleep(5)

        if STA.is_connected():
            yield from app.render_template(resp, "login.tpl", args=(req,))
        else:
            error = "rede"
            yield from app.render_template(resp, "error.tpl", args=(error,))

    else:
        yield from app.render_template(resp, "404.tpl")

@app.route("/finish")
def index(req, resp):
    global settings
    yield from picoweb.start_response(resp)
    if req.method == "POST":
        yield from req.read_form_data()
        settings["HOST"] = req.form["host"]
        settings["USERNAME"] = req.form["username"]
        settings["PASSWORD"] = req.form["password"]

        write_settings(settings)

        if login():
            print("Login realizado com sucesso", token)
            yield from app.render_template(resp, "finish.tpl", args=(settings,))
        else:
            error = "login"
            yield from app.render_template(resp, "error.tpl", args=(error,))


    else:
        yield from app.render_template(resp, "404.tpl")

settings = read_settings()
print("SETTINGS", settings)

websocket = False
token = None
device_id = None

mode_pin = Pin(MODE_PIN, Pin.IN, Pin.PULL_UP)
int_pin = Pin(INT_PIN, Pin.IN, Pin.PULL_UP)
output_pin = Pin(OUTPUT_PIN, Pin.OUT) 

def login():
    """ Log in through the REST api and get the valid token """
    global token

    url = 'http://' + settings["HOST"] + '/api/v1/auth/login/'
    data = {
        "username": settings["USERNAME"],
        "password": settings["PASSWORD"]
    }
    headers = {
        "content-type": 'application/json'
    }
    try:
        r = requests.post(url=url, headers=headers, json=data)
        token = r.json()["key"]
    except Exception as e:
        # print(e)
        return False
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
                print("Old pin value:", output_pin.value())
                output_pin.value(state)
        except TypeError:  # needed to avoid None return while interrupt handler is working
            pass


int_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=toggle_state)

if mode_pin.value():
    print("### WEBSERVER MODE ###")
    AP.connect()
    app.run(debug=True, host='0.0.0.0', port='80')

else:
    print("### NODE MODE ###")

    STA.connect()
    STA.configure(settings["SSID"], settings["SSID_PASSWORD"])
    # TODO: improve flow here
    while not login():
        pass
    print("TOKEN", token)
    while not get_device_id():
        pass
    print("Device id", device_id)
    connect_ws()
    wait_4_messages()
