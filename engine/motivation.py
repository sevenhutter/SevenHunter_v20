def evaluate_motivation(level_home, level_away):
    """
    SevenHunter v20 Motivation Analyzer (base version)

    level scale:
    - 3 : must-win / qualification pressure
    - 2 : normal motivation
    - 1 : relaxed / low strength match
    """
    home_motivation = level_home / 3
    away_motivation = level_away / 3

    return {
        "home_motivation": home_motivation,
        "away_motivation": away_motivation
    }
