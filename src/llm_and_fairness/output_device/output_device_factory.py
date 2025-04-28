from output_device.jupyter_output_device import JupyterOutputDevice
from output_device.standard_output_device import StandardOutputDevice


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