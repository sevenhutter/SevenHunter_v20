def project_xg(home_shots, away_shots, home_quality=1.0, away_quality=1.0):
    """
    SevenHunter v20 xG Projector (base version)
    """
    home_xg = home_shots * 0.10 * home_quality
    away_xg = away_shots * 0.10 * away_quality

    return {
        "home_xg": home_xg,
        "away_xg": away_xg
    }
