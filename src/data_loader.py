import pandas as pd

def load_raw_data():
    """Load all 4 raw datasets"""
    renewal = pd.read_csv('../data/raw/renewal_calls.csv', low_memory=False)
    billings = pd.read_csv('../data/raw/billings.csv', low_memory=False)
    cc_calls = pd.read_csv('../data/raw/cc_calls.csv', low_memory=False)
    emails = pd.read_csv('../data/raw/emails.csv', low_memory=False)
    return renewal, billings, cc_calls, emails
