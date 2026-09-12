from sklearn.isotonic import IsotonicRegression


class ProbabilityCalibrator:

    def __init__(self):
        self.model = IsotonicRegression(
            out_of_bounds="clip"
        )

    def fit(self, probabilities, outcomes):
        self.model.fit(probabilities, outcomes)

    def transform(self, probabilities):
        return self.model.predict(probabilities)
