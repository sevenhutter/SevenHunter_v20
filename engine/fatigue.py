def calculate_fatigue(minutes_last_game, days_rest):
    """
    SevenHunter v20 Fatigue Calculator (base version)
    """
    fatigue_score = (minutes_last_game / 90) * (1 - min(days_rest / 7, 1))

    return {
        "fatigue_score": round(fatigue_score, 3)
    }
