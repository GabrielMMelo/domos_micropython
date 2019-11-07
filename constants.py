import network
import ubinascii


INT_PIN     = 14
OUTPUT_PIN  = 12
MODE_PIN    = 13
MAC_ADDRESS = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
