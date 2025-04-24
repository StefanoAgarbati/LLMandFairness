from src.llm_and_fairness.output_device.output_device import OutputDevice


class StandardOutputDevice(OutputDevice):
    def out(self, aMessage):
        print(aMessage)