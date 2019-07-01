<img align="right" width="200" height="200" src="https://github.com/GabrielMMelo/pyiot-api/blob/master/docs/logo.png" alt="PyIoT's logo">

# PyIoT
> Your home controller powered by python

This project was splitted out in 3 repositories:
- [Api application](https://github.com/GabrielMMelo/pyiot-api.git) - Django, DRF, Django Channels, PostgreSQL & Redis 
- [Front-end application](https://github.com/GabrielMMelo/pyiot-fe.git) - React & Redux
> It's not python, but is okay...

- [MicroPython application](https://github.com/GabrielMMelo/pyiot-mp.git) - MicroPython

**PyIoT** aims to be a scalable home controller application which you can easily add/remove nodes and get the whole controll of your home devices.

## Running

To get started with the PyIoT, just follow this steps below.

#### Install device upload tools (supposing that you'll use ESP32 as your node)

```shell
mkvirtualenv pyiot-esp32
pip install esptool mpfshell
```

#### Download the latest MicroPython's firmware version

- Access [here!](https://micropython.org/download#esp32)

#### Erase actual and then upload the firmware 
```shell
esptool.py --chip esp32 --port /dev/TTY_PORT -- baud 460800 erase_flash
esptool.py --chip esp32 --port /dev/TTY_PORT --baud 460800 write_flash -z 0x1000 FIRMWARE_PATH
```

> Make sure you change the TTY\_PORT for the port where your device is connected and FIRMWARE\_PATH for the absolute path where you downloaded the firmware. 

#### Clone this repo
```shell
git clone https://github.com/GabrielMMelo/pyiot-mp
cd pyiot-mp/
```

#### Upload code to esp32 using `mpfshell`

- Take a look [here](https://github.com/wendlers/mpfshell) to get started with the tool.

#### Set the device ID in `main.py` for the same that you set in the api.

_e.g._

```python
ID_DEVICE = 1
```
#### Run the application
Just power the device and take control of your home!

> You'll also need to follow the steps described in the two anothers repos as well

## Deploying
**TODO***

## Testing
**TODO***

## Contributing
**TODO***
