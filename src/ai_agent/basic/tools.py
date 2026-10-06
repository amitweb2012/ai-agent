from datetime import datetime
from pathlib import Path
import random
import secrets
import string


def get_current_time() -> str:
    """Return the current local date and time."""
    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


def roll_dice() -> int:
    """Return a random number between 1 and 6."""
    return random.randint(1, 6)


def generate_password(length: int = 12) -> str:
    """Generate a cryptographically secure random password."""
    if length < 4:
        raise ValueError("Password length must be at least 4")
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


def read_text_file(path: Path) -> str:
    """Read a UTF-8 text file and return its contents."""
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return "Error: File not found."
