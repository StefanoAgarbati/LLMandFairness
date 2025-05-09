class CalculateFairnessMetricsUseCase:

    def __init__(self, fairness_metrics, split_repository, prediction_repository, encoder):
        self.split_repository = split_repository
        self.prediction_repository = prediction_repository
        self.fairness_metrics = fairness_metrics
        self.encoder = encoder

    def get_fairness_group_metrics(self, dataset_name, metrics, sensitive_groups):
        split = self.split_repository.get_split_by_name(dataset_name)
        prediction = self.prediction_repository.get_prediction_by_name(dataset_name)
        metrics_list = self.get_metrics_list(metrics)
        sensitive_list =self.get_sensitive_list(sensitive_groups)

        ds_decoded = self.decode_dataset(split.get_X_test())
        group_metrics = self.compute_group_metrics(ds_decoded, prediction.get_y_pred(), split.get_y_test(), metrics_list, sensitive_list)
        return group_metrics

    def get_metrics_list(self, metrics):
        res = metrics.split(",")
        print(f"CalculateFairnessUC->get_metrics_list->{res}")
        return res

    def get_sensitive_list(self, sensitive_groups):
        res = sensitive_groups.split(",")
        print(f"CalculateFairnessUC->get_sensitive_list->{res}")
        return res

    def decode_dataset(self, dataset):
        ds = dataset.copy()
        for column in dataset.columns:
            if self.encoder.has_encoder_for(column):
                ds[column] = self.encoder.decode_attribute(dataset, column)
        return ds

    def compute_group_metrics(self, ds_decoded, y_pred, y_true, metrics_list, sensitive_list):
        results = []
        for sensitive in sensitive_list:
            result = self.fairness_metrics.by_groups(metrics_list, y_true, y_pred, ds_decoded[sensitive])
            results.append(result)
        return results


