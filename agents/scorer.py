def score_leads(leads):
    for l in leads:
        score = 0
        if "Director" in l["Title"]:
            score += 30
        if l["Funding"] == "Series B":
            score += 20
        if "Cambridge" in l["HQ"]:
            score += 10
        l["Probability"] = score
    return leads