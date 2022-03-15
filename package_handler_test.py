import unittest
from package_handler import *

class PackageHandlerTest(unittest.TestCase):

    def test_standard_small_package(self):
        dimensions = [20, 40, 50]
        weight=10
        package=PackageHandler().get_package_type(dimensions, weight)

        self.assertEqual(package["type"], "small")
        self.assertEqual(package["cost"], 5)

    def test_standard_medium_package(self):
        dimensions = [180, 280, 380]
        weight=10
        package=PackageHandler().get_package_type(dimensions, weight)

        self.assertEqual(package["type"], "medium")
        self.assertEqual(package["cost"], 7.50)

    def test_standard_large_package(self):
        dimensions = [240, 350, 550]
        weight=10
        package=PackageHandler().get_package_type(dimensions, weight)

        self.assertEqual(package["type"], "large")
        self.assertEqual(package["cost"], 8.50)
    
    def test_weight_over_25_returns_none(self):
        dimensions = [400, 600, 250]
        weight=30
        package=PackageHandler().get_package_type(dimensions, weight)
        self.assertEqual(package, None)

    def test_dimensions_exceed_large_package_returns_none(self):
        dimensions = [401, 600, 250]
        weight=10
        package=PackageHandler().get_package_type(dimensions, weight)

        self.assertEqual(package, None)

    def test_weight_exactly_25_returns_package(self):
        dimensions = [240, 350, 550]
        weight=25
        package=PackageHandler().get_package_type(dimensions, weight)

        self.assertEqual(package["type"], "large")
        self.assertEqual(package["cost"], 8.50)

    def test_negative_inputs_throws_error(self):
        dimensions = [40, -20, 250]
        weight=10

        with self.assertRaises(ValueError):
            PackageHandler().validate_input(dimensions, weight)

    def test_invalid_dimension_length_throws_error(self):
        dimensions = [100, 100]
        weight=10

        with self.assertRaises(ValueError):
            PackageHandler().validate_input(dimensions, weight)

if __name__ == '__main__':
    unittest.main()