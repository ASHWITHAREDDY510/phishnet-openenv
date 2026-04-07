def grade(pred, actual):
    if pred == actual:
        return 1.0

    # partial credit
    if pred == "spam" and actual == "phishing":
        return 0.5

    return 0.0