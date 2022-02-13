

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("lightbulb: turn on")

    def turn_off(self):
        print("lightbulb: turn off")


class Fan(Switchable):
    def turn_on(self):
        print("fan: turn on")

    def turn_off(self):
        print("fan: turn off")

class ElectricPowerSwitch:
    
    def __init__(self, l: Switchable):
        self.util = l
        self.on = False


    def press(self):
        if self.on:
            # appliances is on
            self.util.turn_off()
            self.on = False
        else:
            # appliances is off
            self.util.turn_on()
            self.on = True


if __name__ == '__main__':
    l = LightBulb()
    f = Fan()
    switch = ElectricPowerSwitch(f)
    switch.press()
    switch.press()