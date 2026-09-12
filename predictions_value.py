def calculate_edge(model_probability, market_probability):
    return model_probability - market_probability


def expected_value(probability, decimal_odds):
    return (
        probability * (decimal_odds - 1)
        - (1 - probability)
    )
