import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from env.environment import PhishNetEnv

env = PhishNetEnv(difficulty="hard")

state = env.reset()

done = False

while not done:
    print("\nEmail:", state.text)

    text = state.text.lower()

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
    import time

while True:
    time.sleep(60)