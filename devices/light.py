from .base import Device

class Light(Device):
    name = "Light"
    msg_start = "Light switched on"
    msg_stop = "Light switched off"