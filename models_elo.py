class EloModel:
    def __init__(self, k_factor=20, home_advantage=50):
        self.k_factor = k_factor
        self.home_advantage = home_advantage
        self.ratings = {}

    def rating(self, team):
        return self.ratings.get(team, 1500)

    def win_probability(self, team_a, team_b, home=False):
        rating_a = self.rating(team_a)
        rating_b = self.rating(team_b)

        if home:
            rating_a += self.home_advantage

        return 1 / (
            1 + 10 ** ((rating_b - rating_a) / 400)
        )

    def update(self, team_a, team_b, result, home=False):
        probability = self.win_probability(
            team_a,
            team_b,
            home
        )

        rating_a = self.rating(team_a)
        rating_b = self.rating(team_b)

        change = self.k_factor * (result - probability)

        self.ratings[team_a] = rating_a + change
        self.ratings[team_b] = rating_b - change
