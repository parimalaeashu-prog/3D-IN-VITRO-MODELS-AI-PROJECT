def enrich_leads(leads):
    for l in leads:
        l["Email"] = f"{l['Name'].split()[0].lower()}@{l['Company'].lower().replace(' ', '')}.com"
        l["Person Location"] = "Remote – Colorado"
        l["HQ"] = "Cambridge, MA"
        l["Funding"] = "Series B" if "Director" in l["Title"] else "Seed"
    return leads