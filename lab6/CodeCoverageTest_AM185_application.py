"""
Test cases targeting high line (code) coverage for calculate_discount.
Achieves 100% line coverage.
"""
import unittest
from calculator import calculate_discount

class TestCalculatorCodeCoverage(unittest.TestCase):
    def test_member_expensive_item(self):
        # is_member=True, price > 100  → 15% discount
        result = calculate_discount(150, True)
        self.assertAlmostEqual(result, 150 * 0.85)

    def test_member_cheap_item(self):
        # is_member=True, price <= 100 → 10% discount
        result = calculate_discount(80, True)
        self.assertAlmostEqual(result, 80 * 0.90)

    def test_non_member_expensive_item(self):
        # is_member=False, price > 100 → 5% discount
        result = calculate_discount(200, False)
        self.assertAlmostEqual(result, 200 * 0.95)

    def test_non_member_cheap_item(self):
        # is_member=False, price <= 100 → 0% discount
        result = calculate_discount(50, False)
        self.assertAlmostEqual(result, 50)

if __name__ == '__main__':
    unittest.main()
