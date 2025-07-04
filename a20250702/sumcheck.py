def is_valid(equation: str) -> list[int]:
    if not isinstance(equation, str) or not equation:
        return []
    if equation.count('+') != 1 or equation.count('=') != 1:
        return []
    if equation.index('+') >= equation.index('=') - 1:
        return []
    if not all(c.isdigit() or c in '+=' for c in equation):
        return []
    return [int(part) for part in equation.replace('=', '+').split('+') if part.isdigit()]

def get_result(equation):
    values = is_valid(equation)
    if len(values) != 3:
        return "ERROR"
    return "PASS" if sum(values[:2]) == values[2] else "FAIL"

# 25+61=100
# 1 ~ 5자리수 덧셈 수식이 맞는지 확인하는 프로그램
# 띄어쓰기 없음
def test_pass():
    assert get_result("25+61=86") == "PASS"
    assert get_result("12345+12345=24690") == "PASS"

def test_error():
    assert get_result("5++5=10") == "ERROR"
    assert get_result("12345+=123") == "ERROR"

def test_fail():
    assert get_result("10000+1=10002") == "FAIL"
