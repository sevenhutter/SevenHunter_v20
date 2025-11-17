def analyze_odds_drift(open_home, open_draw, open_away,
                       live_home, live_draw, live_away):
    """
    SevenHunter v20 Odds Drift Analyzer (base version)
    """
    drift_home = live_home - open_home
    drift_draw = live_draw - open_draw
    drift_away = live_away - open_away

    return {
        "drift_home": drift_home,
        "drift_draw": drift_draw,
        "drift_away": drift_away
    }
