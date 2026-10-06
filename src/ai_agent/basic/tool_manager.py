from pathlib import Path
import re

from .tools import generate_password, get_current_time, read_text_file, roll_dice

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def execute_tool(user_input: str) -> str | None:
    """Route simple natural-language requests to deterministic tools."""
    text = user_input.lower().strip()

    if "time" in text or "clock" in text:
        return get_current_time()
    if "dice" in text or re.search(r"\bdie\b", text):
        return f"You rolled {roll_dice()}"
    if "password" in text:
        return generate_password()

    for keyword in ("summarize", "explain"):
        if text.startswith(keyword):
            filename = user_input[len(keyword):].strip()
            if not filename:
                return f"Please provide a file name after '{keyword}'."
            content = read_text_file(DATA_DIR / filename)
            label = "Summary" if keyword == "summarize" else "Explanation"
            return f"{label} of {filename}:\n{content}"

    return None
