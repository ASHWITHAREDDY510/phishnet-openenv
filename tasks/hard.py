def get_hard_data():
    return [
        {"text": "Important: unusual login detected, review activity", "label": "phishing"},
        {"text": "Invoice attached for last transaction", "label": "safe"},
        {"text": "You have been selected for exclusive reward program", "label": "spam"},
        {"text": "Verify your account to avoid suspension", "label": "phishing"},
        {"text": "Team meeting rescheduled to 3 PM", "label": "safe"},
        {"text": "Claim your free vacation now!!!", "label": "spam"}
    ]