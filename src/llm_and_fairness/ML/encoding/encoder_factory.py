from src.llm_and_fairness.ML.encoding.sk_learn_label_encoder import SkLearnNominalEncoder


class EncoderFactory:

    @staticmethod
    def create_encoder(encoder_type, categories=None):
        match encoder_type:
            case EncoderType.NOMINAL_ENCODER:
                return EncoderFactory.create_nominal_encoder()
            case EncoderType.ORDINAL_ENCODER:
                return EncoderFactory.create_ordinal_encoder(categories)
            case _:
                raise Exception("The encoder type provided doesn't exist")

    @staticmethod
    def create_nominal_encoder():
        return SkLearnNominalEncoder()

    @staticmethod
    def create_ordinal_encoder(categories):
        pass


class EncoderType:
    NOMINAL_ENCODER = 'nominal'
    ORDINAL_ENCODER = 'ordinal'