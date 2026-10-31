
import re

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return " ".join(text.split())


def contains_answer(actual: str, expected: str) -> bool:
    actual = normalize(actual)
    expected = normalize(expected)

    if not expected:
        return False

    return f" {expected} " in f" {actual} "
