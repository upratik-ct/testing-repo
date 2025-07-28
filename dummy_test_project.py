"""dummy_test_project.py

This module provides a simulation framework for processing data, user management, and utility functions.
It includes:
- Config and Processor classes for configuration and data processing simulation.
- Utility functions for text normalization, palindrome checking, and word counting.
- A User class for dummy user representation.
- A main block that simulates processing and demonstrates utility functions.

Author: [Your Name]
Version: 1.0.0
"""

import os
import sys
import time
from typing import List, Dict, Optional

# Global variable for simulation
VERSION = "1.0.0"

def log(message: str) -> None:
    """
    Logs a message with a timestamp.

    Args:
        message (str): The message to log.
    """
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")

class Config:
    """
    Configuration handler for storing and retrieving settings.

    Attributes:
        settings (Dict[str, str]): Dictionary of configuration settings.
    """

    def __init__(self, settings: Optional[Dict[str, str]] = None) -> None:
        """
        Initializes the Config object.

        Args:
            settings (Optional[Dict[str, str]]): Initial settings dictionary.
        """
        self.settings = settings or {}
        log("Config initialized.")

    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """
        Retrieves a configuration value.

        Args:
            key (str): The configuration key.
            default (Optional[str]): Default value if key is not found.

        Returns:
            Optional[str]: The configuration value or default.
        """
        return self.settings.get(key, default)

    def set(self, key: str, value: str) -> None:
        """
        Sets a configuration value.

        Args:
            key (str): The configuration key.
            value (str): The value to set.
        """
        self.settings[key] = value
        log(f"Setting updated: {key} = {value}")

class Processor:
    """
    Simulates a data processor using provided configuration.

    Attributes:
        config (Config): Configuration object.
        status (str): Current status of the processor.
    """

    def __init__(self, config: Config) -> None:
        """
        Initializes the Processor.

        Args:
            config (Config): Configuration object.
        """
        self.config = config
        self.status = "initialized"
        log("Processor created.")

    def process_data(self, data: List[int]) -> Dict[str, float]:
        """
        Processes a list of integers and computes statistics.

        Args:
            data (List[int]): List of integers to process.

        Returns:
            Dict[str, float]: Dictionary with mean, max, and min values.
        """
        log("Processing data...")
        if not data:
            return {"mean": 0, "max": 0, "min": 0}
        return {
            "mean": sum(data) / len(data),
            "max": max(data),
            "min": min(data),
        }

    def reset(self) -> None:
        """
        Resets the processor state.
        """
        self.status = "reset"
        log("Processor state reset.")

def simulate_processing() -> None:
    """
    Simulates a processing workflow using Config and Processor.
    Runs multiple iterations of data processing and logs results.
    """
    cfg = Config({"mode": "test"})
    proc = Processor(cfg)
    for i in range(10):
        data = list(range(i * 10))
        result = proc.process_data(data)
        log(f"Run {i}: {result}")
    proc.reset()

# Utilities
def normalize(text: str) -> str:
    """
    Normalizes text by stripping whitespace and converting to lowercase.

    Args:
        text (str): The text to normalize.

    Returns:
        str: Normalized text.
    """
    return text.strip().lower()

def is_palindrome(word: str) -> bool:
    """
    Checks if a word or phrase is a palindrome (case-insensitive, ignores whitespace).

    Args:
        word (str): The word or phrase to check.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    word = normalize(word)
    return word == word[::-1]

def word_count(sentence: str) -> Dict[str, int]:
    """
    Counts the occurrences of each word in a sentence.

    Args:
        sentence (str): The sentence to analyze.

    Returns:
        Dict[str, int]: Dictionary mapping words to their counts.
    """
    words = normalize(sentence).split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

# Dummy class for users
class User:
    """
    Represents a dummy user with username and email.

    Attributes:
        username (str): The user's username.
        email (str): The user's email address.
    """

    def __init__(self, username: str, email: str) -> None:
        """
        Initializes a User object.

        Args:
            username (str): The user's username.
            email (str): The user's email address.
        """
        self.username = username
        self.email = email

    def display(self) -> None:
        """
        Displays the user's information.
        """
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