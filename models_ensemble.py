class EnsembleModel:

    def __init__(
        self,
        elo_weight=0.40,
        ml_weight=0.60
    ):
        self.elo_weight = elo_weight
        self.ml_weight = ml_weight

    def predict(self, features):

        elo_probability = features["elo_probability"]
        ml_probability = features["ml_probability"]

        probability = (
            self.elo_weight * elo_probability
            + self.ml_weight * ml_probability
        )

        return probability
