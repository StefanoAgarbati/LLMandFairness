class ToolCall:
    def __init__(self, data):
        self.data =data

    def get_data(self):
        return self.data

    def get_name(self):
        return self.data['name']

    def get_args(self):
        return self.data['args']