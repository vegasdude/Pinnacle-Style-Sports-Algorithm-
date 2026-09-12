def american_to_probability(odds: int) -> float:
    """Convert American odds to implied probability."""
    if odds > 0:
        return 100 / (odds + 100)

    return abs(odds) / (abs(odds) + 100)


def remove_vig(prob_a: float, prob_b: float):
    """Normalize two-way market probabilities."""
    total = prob_a + prob_b

    return (
        prob_a / total,
        prob_b / total,
    )
