class TaxCalculator:
    LOWER = [0, 30000, 100000]
    UPPER = [30000, 100000, float('inf')]
    RATES = [0.1, 0.2, 0.3]

    def calculate_tax(self, income: float) -> float:
        tax = 0.0
        for lb, ub, r in zip(self.LOWER, self.UPPER, self.RATES):
            tax += self._tax_in_range(income, lb, ub) * r
        return tax

    @staticmethod
    def _tax_in_range(income: float, lower_bound, upper_bound) -> float:
        return max(0.0, min(income, upper_bound) - lower_bound)


def test_calculate_tax():
    calc = TaxCalculator()
    assert calc.calculate_tax(15000) == 1500.0
    assert calc.calculate_tax(31000) == 3200
    assert calc.calculate_tax(100200) == 17060
