from output_device.output_device import OutputDevice
from IPython.display import display, Markdown


class JupyterOutputDevice(OutputDevice):
    def out_markdown(self, data):
        display(Markdown(data))

    def out_figure(self, figure):
        display(figure)

    def out(self, aMessage):
        display(aMessage)
