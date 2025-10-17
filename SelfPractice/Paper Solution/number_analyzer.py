class NumberAnalyzer:
    """Analyze numeric properties and perform computations."""

    def __init__(self, value: int):
        self.value = value

    def is_multiple_of(self, m: int) -> bool:
        """Check if value is a multiple of m."""
        return self.value % m == 0

    def is_even(self) -> bool:
        """Check if number is even without using %, /, or *."""
        return (self.value & 1) == 0  # bitwise check

    def sum_of_squares_below(self) -> int:
        """Sum of squares of all positive integers smaller than value."""
        total = 0
        for i in range(1, self.value):
            total += i * i
        return total

    def sum_of_odd_squares_below(self) -> int:
        """Sum of squares of all odd numbers below value."""
        total = 0
        for i in range(1, self.value, 2):
            total += i * i
        return total
    
a = NumberAnalyzer(5)
b = a
value = 10
print(a.value)

obj = NumberAnalyzer(7)
f = obj.is_even
print(f())


print(NumberAnalyzer(4).sum_of_squares_below())

