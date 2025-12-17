import pandas as pd
from agents.identifier import identify_leads
from agents.enricher import enrich_leads
from agents.scorer import score_leads

def run_pipeline(keywords):
    leads = identify_leads(keywords)
    enriched = enrich_leads(leads)
    scored = score_leads(enriched)
    return pd.DataFrame(scored).sort_values("Probability", ascending=False)