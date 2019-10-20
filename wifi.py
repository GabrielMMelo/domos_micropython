import network


class Sta():
    def __init__(self):
        self.sta_if = network.WLAN(network.STA_IF)
    
    def __str__(self):
        return self.sta_if.ifconfig()

    def configure(self, essid, password):
        self.sta_if.connect(essid, password)

    def connect(self):
        self.sta_if.active(True)

    def is_connected(self):
        return self.sta_if.isconnected()

    def disconnect(self):
        self.sta_if.active(False)

class Ap():
    def __init__(self):
        self.ap_if = network.WLAN(network.AP_IF)
    
    def __str__(self):
        return self.ap_if.ifconfig()

    def configure(self, essid, password):
        self.ap_if.config(authmode=3, essid=essid, password=password)

    def connect(self):
        self.ap_if.active(True)

    def disconnect(self):
        self.ap_if.active(False)

STA = Sta()
AP = Ap()
