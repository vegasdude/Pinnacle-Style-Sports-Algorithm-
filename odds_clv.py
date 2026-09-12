def calculate_clv(
    opening_probability,
    closing_probability
):
    """
    Positive value means the probability
    moved favorably relative to the opening market.
    """

    return closing_probability - opening_probability
