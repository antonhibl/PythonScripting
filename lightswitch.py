class LightSwitch:
    def __init__(self):
        self.switch_is_on = False

    def turn_on(self):
        # turn the switch on
        self.switch_is_on = True

    def turn_off(self):
        # turn the switch off
        self.switch_is_on = False

    def is_on(self):
        # check if the switch is on
        print(self.switch_is_on)


o_lightswitch = LightSwitch()

o_lightswitch.is_on()
o_lightswitch.turn_on()
o_lightswitch.is_on()
o_lightswitch.turn_off()
o_lightswitch.is_on()
