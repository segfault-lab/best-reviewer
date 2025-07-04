import pytest

def check_str(text: str) -> bool:
    if not isinstance(text, str) or not text:
        return False
    return True

def split_and_convert(values: list[str]) -> int | None:
    results = 0
    for val in values:
        if not val.isdigit():
            return None
        results += int(val)
    return results

def split_and_sum(text: str):
    if not check_str(text):
        return 0
    values = text.split("-")
    return split_and_convert(values)

def test_split_and_sum():
    assert split_and_sum("0-1-2-3-4-5") == 15
    assert split_and_sum("0-1-2-3-4-5a") is None