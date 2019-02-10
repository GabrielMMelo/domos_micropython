import network
from settings import STA_PWD, STA_PWD

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(STA_SSID, STA_PWD)
