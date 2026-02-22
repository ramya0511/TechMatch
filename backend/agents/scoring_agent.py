def calculate_score(company_info, fit_info):

    overlap = fit_info.get("overlap_score", 0)
    intent = fit_info.get("intent_score", 0)

    lead_score = (overlap * 6) + (intent * 4)

    if lead_score > 70:
        category = "Hot"
    elif lead_score > 40:
        category = "Warm"
    else:
        category = "Cold"

    return {
        "lead_score": lead_score,
        "category": category
    }