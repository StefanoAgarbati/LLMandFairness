from output_device.output_device import OutputDevice


class StandardOutputDevice(OutputDevice):
    def out(self, aMessage):
        print(aMessage)