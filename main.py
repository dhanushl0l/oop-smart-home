from devices import Fan, Light
from controller import Controller

if __name__ == "__main__":
    # Fan Demo
    fan_ctrl = Controller(Fan())
    fan_ctrl.power_on()
    fan_ctrl.power_off()

    print("-" * 20)

    # Light Demo
    light_ctrl = Controller(Light())
    light_ctrl.power_on()
    light_ctrl.power_off()