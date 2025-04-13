class OutputDevice:
    def out(self, aMessage):
        pass


class StandardOutputDevice(OutputDevice):
    def out(self, aMessage):
        print(aMessage)


class OutputDeviceFactory:

    @staticmethod
    def createOutputDevice(outputDeviceType):
        match outputDeviceType:
            case OutputDeviceType.Standard:
                return OutputDeviceFactory.createStandardOutputDevice()

    @staticmethod
    def createStandardOutputDevice():
        return StandardOutputDevice()


class OutputDeviceType:
    Standard = "standard"

