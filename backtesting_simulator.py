class Backtester:

    def __init__(self, starting_bankroll=1000):
        self.starting_bankroll = starting_bankroll
        self.bankroll = starting_bankroll
        self.results = []

    def record(self, won, stake, profit):
        self.bankroll += profit

        self.results.append({
            "won": won,
            "stake": stake,
            "profit": profit,
            "bankroll": self.bankroll
        })

    def roi(self):
        total_staked = sum(
            result["stake"]
            for result in self.results
        )

        total_profit = sum(
            result["profit"]
            for result in self.results
        )

        if total_staked == 0:
            return 0

        return total_profit / total_staked
