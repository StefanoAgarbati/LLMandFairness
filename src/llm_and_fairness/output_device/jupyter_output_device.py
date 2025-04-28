from output_device.output_device import OutputDevice
from IPython.display import display, Markdown


class JupyterOutputDevice(OutputDevice):
    def out_markdown(self, data):
        pass

    def out_figure(self, figure):
        pass

    def out(self, aMessage):
        display(Markdown(aMessage))
