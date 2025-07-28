import os
import sys
import time
from typing import List, Dict, Optional

# Global variable for simulation
VERSION = "1.0.0"

def log(message: str) -> None:

    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")

class Config:

    def __init__(self, settings: Optional[Dict[str, str]] = None) -> None:
        self.settings = settings or {}
        log("Config initialized.")

    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        return self.settings.get(key, default)

    def set(self, key: str, value: str) -> None:
        self.settings[key] = value
        log(f"Setting updated: {key} = {value}")

class Processor:


    def __init__(self, config: Config) -> None:
        self.config = config
        self.status = "initialized"
        log("Processor created.")

    def process_data(self, data: List[int]) -> Dict[str, float]:

        log("Processing data...")
        if not data:
            return {"mean": 0, "max": 0, "min": 0}
        return {
            "mean": sum(data) / len(data),
            "max": max(data),
            "min": min(data),
        }

    def reset(self) -> None:

        self.status = "reset"
        log("Processor state reset.")

def simulate_processing() -> None:

    cfg = Config({"mode": "test"})
    proc = Processor(cfg)
    for i in range(10):
        data = list(range(i * 10))
        result = proc.process_data(data)
        log(f"Run {i}: {result}")
    proc.reset()

# Utilities
def normalize(text: str) -> str:
    return text.strip().lower()

def is_palindrome(word: str) -> bool:
    word = normalize(word)
    return word == word[::-1]

def word_count(sentence: str) -> Dict[str, int]:
    words = normalize(sentence).split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

# Dummy class for users
class User:

    
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def display(self) -> None:
        print(f"User: {self.username} ({self.email})")

# Main trigger (simulate heavy code)
if __name__ == "__main__":
    simulate_processing()
    log("Simulation complete.")
    users = [User(f"user{i}", f"user{i}@example.com") for i in range(5)]
    for user in users:
        user.display()
    sentences = ["Madam In Eden I'm Adam", "Hello world", "Racecar"]
    for s in sentences:
        print(f"'{s}' is palindrome? {is_palindrome(s)}")
