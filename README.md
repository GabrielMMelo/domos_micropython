<img align="right" width="250" height="191" src="https://github.com/GabrielMMelo/pyiot-api/blob/master/docs/logo.png" alt="DOMOS logo">

# DOMOS
> Domotics Open Source project

This project was splitted out in 4 repositories:
- [API REST (ASGI/WSGI) application](https://github.com/GabrielMMelo/domos_api.git) - Nginx, Daphne, Gunicorn, Django, DRF, Django Channels, PostgreSQL & Redis 
- [Front-end Web application](https://github.com/GabrielMMelo/pyiot-fe.git) - React & Material UI
- [Front-end Mobile application](https://github.com/GabrielMMelo/pyiot-fe.git) - React-Native 
- [MicroPython application](https://github.com/GabrielMMelo/pyiot-mp.git) - MicroPython

**DOMOS** is an scalable home controller application which you can easily add/remove nodes and have secure remote control of your home devices.

This repo contains the implementation of the nodes logic using MicroPython, a lightweight Python3 implementation for embeded devices. At this time, **DOMOS** was tested with `ESP8266` and `ESP32` ports.

## How it works?
Each `node` in the **DOMOS** architecture is the responsible for acting with the extern environment. "Acting" means changing a microcontroller GPIO state, for now.

The node authenticates over HTTPS API requests ([this repo](https://github.com/GabrielMMelo/domos-api)) using its `MAC ADDRESS` with the user's provided credentials. Once it's done, it stablishes a persistent and secure Web Socket connection with the WS Server (Django Channels), sending eventual changes on its state and also listening to changes made by React or React Native applications.


## Running

To get started with the **DOMOS**, just follow this steps below.

#### Install device upload tools (supposing that you'll use ESP32 as your node)

```shell
mkvirtualenv domos-micropython
pip install esptool adafruit-ampy
```

#### Download the latest DOMOS firmware version

- Access [here!](https://github.com/GabrielMMelo/domos_micropython/releases)

#### Erase flash memory and then upload the firmware 
```shell
esptool.py --port /dev/TTY_PORT --baud 115200 erase_flash
esptool.py --port /dev/TTY_PORT --baud 115200 write_flash -z 0x1000 FIRMWARE_PATH
```

> Make sure you replace `TTY\_PORT` with the port where your device is connected and `FIRMWARE\_PATH` for the absolute path where you downloaded the firmware. 

## Developing

### ESP8266
- In order to build custom firmwares for ESP8266 port, you'll need to clone MicroPython project and a successful installation of the OpenSource ESP SDK. The step-by-step tutorial can be found [here](https://github.com/micropython/micropython/tree/master/ports/esp8266#build-instructions)

### ESP32
- `TODO`

#### Clone this repo
```shell
git clone https://github.com/GabrielMMelo/domos-micropython
cd domos-micropython/
```
#### Copy all files from this repo to your recent MicroPython ESP8266 port modules folder
```shell
mv ./* ../micropython/ports/esp8266/modules/.
```

#### Build and Deploy the firmware
```shell
cd ../micropython/ports/esp8266
make clean && make
esptool.py --port /dev/TTY_PORT --baud 115200 erase_flash
make PORT=/dev/TTY_PORT FLASH_SIZE=32m deploy
```
