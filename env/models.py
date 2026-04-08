from dataclasses import dataclass

@dataclass
class EmailState:
    text: str
    length: int
    has_link: bool
    has_urgent_words: bool