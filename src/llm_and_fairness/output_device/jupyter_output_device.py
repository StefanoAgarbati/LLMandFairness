from output_device.output_device import OutputDevice
from IPython.display import display, Markdown

class JupyterOutputDevice(OutputDevice):
    def out(self, aMessage):
        display(Markdown(aMessage))