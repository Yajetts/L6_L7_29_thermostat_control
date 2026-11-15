"""
Test cases targeting high branch coverage for calculate_discount.
Covers all combinations of the two independent if conditions.
Achieves 100% branch coverage.
"""
import unittest
from calculator import calculate_discount

class TestCalculatorBranchCoverage(unittest.TestCase):
    def test_member_and_price_gt_100(self):
        # Branch: is_member=True, price>100
        result = calculate_discount(150, True)
        self.assertAlmostEqual(result, 150 * 0.85)

    def test_member_and_price_le_100(self):
        # Branch: is_member=True, price<=100
        result = calculate_discount(100, True)
        self.assertAlmostEqual(result, 100 * 0.90)

    def test_non_member_and_price_gt_100(self):
        # Branch: is_member=False, price>100
        result = calculate_discount(120, False)
        self.assertAlmostEqual(result, 120 * 0.95)

    def test_non_member_and_price_le_100(self):
        # Branch: is_member=False, price<=100
        result = calculate_discount(50, False)
        self.assertAlmostEqual(result, 50)

    def test_edge_price_exactly_100_member(self):
        # Explicit edge: price == 100
        result = calculate_discount(100, True)
        self.assertAlmostEqual(result, 90.0)

    def test_edge_price_just_over_100_non_member(self):
        result = calculate_discount(100.01, False)
        self.assertAlmostEqual(result, 100.01 * 0.95)

if __name__ == '__main__':
    unittest.main()
