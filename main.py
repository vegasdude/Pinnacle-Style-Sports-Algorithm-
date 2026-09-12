from odds.implied_probability import (
    american_to_probability,
    remove_vig
)

from models.elo import EloModel
from predictions.value import calculate_edge


def main():

    # Example market
    team_a_odds = -120
    team_b_odds = +105

    raw_a = american_to_probability(team_a_odds)
    raw_b = american_to_probability(team_b_odds)

    market_a, market_b = remove_vig(
        raw_a,
        raw_b
    )

    # Example ELO model
    model = EloModel()

    model.ratings["Team A"] = 1575
    model.ratings["Team B"] = 1500

    prediction = model.win_probability(
        "Team A",
        "Team B",
        home=True
    )

    edge = calculate_edge(
        prediction,
        market_a
    )

    print("=== Sports Algorithm v0.1 ===")
    print(f"Market probability: {market_a:.2%}")
    print(f"Model probability:  {prediction:.2%}")
    print(f"Model edge:        {edge:.2%}")


if __name__ == "__main__":
    main()
