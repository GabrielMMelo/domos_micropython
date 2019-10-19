import network
import ubinascii


INT_PIN     = 18
OUTPUT_PIN  = 19
MODE_PIN    = 21
MAC_ADDRESS = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
