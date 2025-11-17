def national_mode_adjust(home_advantage, motivation_home, motivation_away,
                         neutral_venue=False, second_game=False):
    """
    SevenHunter v20 National Adaptive Mode (base version)

    - home_advantage: 기본 홈 어드벤티지 값 (0~1)
    - motivation_home/motivation_away: 동기 레벨 (0~3)
    - neutral_venue: 중립 경기 여부
    - second_game: 같은 A매치 기간 2번째 경기 여부
    """

    # 중립 경기 → 홈 이점 제거
    if neutral_venue:
        home_adv = 0
    else:
        home_adv = home_advantage

    # 두 번째 경기 → 피로도 패널티
    fatigue_penalty = 0.10 if second_game else 0.0

    adj_home = (home_adv + motivation_home * 0.05) - fatigue_penalty
    adj_away = (motivation_away * 0.05)

    return {
        "adj_home_factor": round(adj_home, 3),
        "adj_away_factor": round(adj_away, 3)
    }
