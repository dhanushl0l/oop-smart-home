from .base import Device

class Fan(Device):
    name = "Fan"
    msg_start = "Fan has started"
    msg_stop = "Fan has stopped"