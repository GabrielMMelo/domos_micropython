import network
import ubinascii


def get_mac():
    return ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()


def set_mac(mac):
    f = open('mac', 'w')
    f.write(mac)
    f.close
