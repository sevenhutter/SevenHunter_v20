def predict_squad(callup_list, injured_list, suspended_list):
    """
    SevenHunter v20 Squad Predictor (base version)
    """
    available = [p for p in callup_list 
                 if p not in injured_list and p not in suspended_list]

    return {
        "available_players": available,
        "total_available": len(available)
    }
