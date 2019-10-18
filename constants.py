import network
import ubinascii


INT_PIN     = 18
OUTPUT_PIN  = 19
MAC_ADDRESS = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
