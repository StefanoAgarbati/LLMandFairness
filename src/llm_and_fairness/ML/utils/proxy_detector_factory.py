from ML.utils.proxy_detector_mutual_info_based import ProxyDetectorMutualInfoBased
from ML.utils.proxy_detectory_tree_based import ProxyDetectorTreeBased


class ProxyDetectorType:
    Tree_based = 'tree_based'
    MutualInfo = 'mutual_info_based'


class ProxyDetectorFactory:

    @staticmethod
    def create(proxy_config):
        if proxy_config['type'] == ProxyDetectorType.MutualInfo:
            return ProxyDetectorMutualInfoBased(proxy_config['metrics'])
        if proxy_config['type'] == ProxyDetectorType.Tree_based:
            return ProxyDetectorTreeBased(proxy_config['splitter'], proxy_config['metrics'])