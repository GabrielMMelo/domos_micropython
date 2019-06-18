# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('zezinho', 'JoseAnjo43')
