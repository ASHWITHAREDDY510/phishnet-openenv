# test change
import random
from tasks.easy import get_easy_data
from tasks.medium import get_medium_data
from tasks.hard import get_hard_data
from grader.grader import grade
from env.models import EmailState

# reproducibility
random.seed(42)

class PhishNetEnv:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.data = self._load_data()
        self.current_email = None
        self.done = False

        self.step_count = 0
        self.max_steps = 5

    def _load_data(self):
        if self.difficulty == "easy":
            return get_easy_data()
        elif self.difficulty == "medium":
            return get_medium_data()
        else:
            return get_hard_data()

    def reset(self):
        self.current_email = random.choice(self.data)
        self.done = False
        self.step_count = 0
        return self._get_state()

    def _get_state(self):
        text = self.current_email["text"]

        return EmailState(
            text=text,
            length=len(text),
            has_link="http" in text,
            has_urgent_words=any(
                word in text.lower()
                for word in ["urgent", "immediately", "verify"]
            ),
        )

    def step(self, action):
        correct_label = self.current_email["label"]

        reward = grade(action, correct_label)

        self.step_count += 1

        if self.step_count >= self.max_steps:
            self.done = True
        else:
            self.done = False
            self.current_email = random.choice(self.data)

        return self._get_state(), reward, self.done, {
            "correct_label": correct_label,
            "step_count": self.step_count
        }