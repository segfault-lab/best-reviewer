class OddEven:
    @staticmethod
    def convert(numbers: list[int]) -> list[str] | None:
        if not numbers:
            return None
        parity = numbers[0] % 2
        if all(n % 2 == parity for n in numbers):
            return None
        return ['O' if n % 2 == 0 else 'X' for n in numbers]