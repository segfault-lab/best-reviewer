import pytest

@pytest.fixture
def ingredient():
    print()
    print("## 닭 준비 ##")
    yield "chicken"
    print("## 치킨 요리 완료 ##")

def test_bbq(ingredient):
    assert ingredient == "chicken"
    print()
    print("## BBQ 치킨 요리 ##")

def test_kfc(ingredient):
    assert ingredient == "chicken"
    print()
    print("## KFC 치킨 요리 ##")