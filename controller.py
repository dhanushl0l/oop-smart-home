from devices.base import Device

class Controller:
    def __init__(self, device: Device):
        self.device = device

    def power_on(self):
        result = self.device.start()
        print(result)

    def power_off(self):
        result = self.device.stop()
        print(result)