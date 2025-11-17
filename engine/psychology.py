def evaluate_psychology(home_streak, away_streak):
    """
    SevenHunter v20 Psychology Model (base version)

    streak:
    - positive: winning streak
    - negative: losing streak
    - 0: neutral
    """
    
    def streak_score(streak):
        if streak > 0:
            return 1 + (streak * 0.05)
        elif streak < 0:
            return 1 + (streak * 0.03)
        return 1
    
    return {
        "home_psy": round(streak_score(home_streak), 3),
        "away_psy": round(streak_score(away_streak), 3)
    }
