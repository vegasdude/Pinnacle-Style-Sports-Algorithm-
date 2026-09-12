def confidence_score(
    model_probability,
    market_probability,
    sample_size
):
    edge = abs(
        model_probability -
        market_probability
    )

    score = min(
        100,
        edge * 200 +
        min(sample_size / 100, 1) * 20
    )

    return round(score, 2)
