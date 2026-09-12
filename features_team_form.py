import pandas as pd


def calculate_form(games, team, window=5):
    team_games = games[
        (games["home_team"] == team) |
        (games["away_team"] == team)
    ].tail(window)

    wins = 0
    points_for = 0
    points_against = 0

    for _, game in team_games.iterrows():

        if game["home_team"] == team:
            scored = game["home_score"]
            allowed = game["away_score"]
        else:
            scored = game["away_score"]
            allowed = game["home_score"]

        points_for += scored
        points_against += allowed

        if scored > allowed:
            wins += 1

    games_played = len(team_games)

    if games_played == 0:
        return {
            "win_rate": 0.5,
            "points_for": 0,
            "points_against": 0
        }

    return {
        "win_rate": wins / games_played,
        "points_for": points_for / games_played,
        "points_against": points_against / games_played
          }
