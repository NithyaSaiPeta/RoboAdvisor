def compute_risk_score(
    age: int,
    annual_income: float,
    investment_horizon: int,
    risk_tolerance: int
):
    """
    risk_tolerance: 1 (low) to 5 (high)
    """

    score = 0

    # Age
    if age < 30:
        score += 25
    elif age < 45:
        score += 20
    elif age < 60:
        score += 10
    else:
        score += 5

    # Income
    if annual_income >= 2_000_000:
        score += 25
    elif annual_income >= 1_000_000:
        score += 20
    else:
        score += 10

    # Horizon
    if investment_horizon > 10:
        score += 25
    elif investment_horizon > 5:
        score += 15
    else:
        score += 5

    # Risk tolerance
    score += risk_tolerance * 5

    return score


def map_risk_profile(score: float):
    if score >= 80:
        return "Aggressive"
    elif score >= 55:
        return "Moderate"
    else:
        return "Conservative"


def get_risk_profile(user_inputs: dict):
    score = compute_risk_score(**user_inputs)
    profile = map_risk_profile(score)

    return {
        "risk_score": score,
        "risk_profile": profile
    }
