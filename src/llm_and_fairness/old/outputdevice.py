from IPython.display import display, Markdown
class OutputDevice:
    def out(self, aMessage):
        pass


class StandardOutputDevice(OutputDevice):
    def out(self, aMessage):
        print(aMessage)

class JupyterOutputDevice(OutputDevice):
    def out(self, aMessage):
        display(Markdown(aMessage))


class OutputDeviceFactory:

    @staticmethod
    def createOutputDevice(outputDeviceType):
        match outputDeviceType:
            case OutputDeviceType.Standard:
                return OutputDeviceFactory.createStandardOutputDevice()
            case OutputDeviceType.Jupyter:
                return OutputDeviceFactory.createJupyterOutputDevice()

    @staticmethod
    def createStandardOutputDevice():
        return StandardOutputDevice()

    @staticmethod
    def createJupyterOutputDevice():
        return JupyterOutputDevice()


class OutputDeviceType:
    Standard = "standard"
    Jupyter = "jupyter"

