from a20250702.aaa_patern_write_test import Account
import pytest

def test_transfer_to():
    acc1 = Account(1000)
    acc2 = Account(500)
    acc1.transfer_to(acc2, 300)
    assert acc1.balance == 700
    assert acc2.balance == 800

def test_transfer_to_insufficient():
    acc1 = Account(1000)
    acc2 = Account(500)
    with pytest.raises(ValueError, match="예금 부족"):
        acc1.transfer_to(acc2, 1200)
    assert acc1.balance == 1000
    assert acc2.balance == 500