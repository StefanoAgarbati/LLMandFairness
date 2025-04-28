from output_device.output_device import OutputDevice


class StandardOutputDevice(OutputDevice):

    def out_markdown(self, data):
        self.out(data)

    def out_figure(self, figure):
        print("I'm sorry but i can't display figures")

    def out(self, aMessage):
        print(aMessage)

