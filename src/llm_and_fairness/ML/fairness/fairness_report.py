class FairnessReport:

    def __init__(self, sensitive_groups, metrics, data):
        self.groups = sensitive_groups
        self.metrics =metrics
        self.data = data

    def get_groups(self):
        groups = ""
        for group in self.groups:
            groups += group + ","
