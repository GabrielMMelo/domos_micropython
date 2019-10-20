# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from constants import MAC_ADDRESS
from settings import read_settings
from wifi import AP, STA

_settings = read_settings()

STA.disconnect()
AP.disconnect()

AP.configure(MAC_ADDRESS, "12345678")
