def calculate_elo(home_elo, away_elo):
    """
    SevenHunter v20 Elo processor (base version)
    """
    expected_home = 1 / (1 + 10 ** ((away_elo - home_elo) / 400))
    expected_away = 1 - expected_home

    return {
        "expected_home": expected_home,
        "expected_away": expected_away
    }
