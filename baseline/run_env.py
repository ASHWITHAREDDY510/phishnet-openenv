import sys
import os
import time

# Fix path for Docker (Hugging Face)
sys.path.append("/app")

from env.environment import PhishNetEnv

# Continuous execution (prevents runtime exit)
while True:
    env = PhishNetEnv(difficulty="hard")
    state = env.reset()
    done = False

    print("\n===== NEW EPISODE =====\n")

    while not done:
        print("Email:", state.text)

        text = state.text.lower()

        # Simple rule-based agent
        if "win" in text or "reward" in text:
            action = "spam"
        elif "account" in text or "login" in text:
            action = "phishing"
        else:
            action = "safe"

        state, reward, done, info = env.step(action)

        print("Action:", action)
        print("Reward:", reward)
        print("Correct:", info["correct_label"])
        print("Step:", info["step_count"])
        print("-" * 40)

    print("\n--- Episode Complete ---\n")

    time.sleep(5)  # small delay before next episode