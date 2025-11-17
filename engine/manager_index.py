def evaluate_manager_style(attack_rate, rotation_rate, risk_rate):
    """
    SevenHunter v20 Manager Index (MTI/MAF) base version
    
    attack_rate: 0~1  (0 = 수비적 / 1 = 공격적)
    rotation_rate: 0~1 (0 = 고정 라인업 / 1 = 잦은 로테이션)
    risk_rate: 0~1 (0 = 안전 플레이 / 1 = 위험 감수 플레이)
    """

    mti = (attack_rate * 0.5) + (risk_rate * 0.3) + (rotation_rate * 0.2)
    maf = 1 + ((attack_rate - 0.5) * 0.1)

    return {
        "MTI": round(mti, 3),
        "MAF": round(maf, 3)
    }
