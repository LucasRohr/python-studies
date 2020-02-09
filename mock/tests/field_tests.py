import unittest
from unittest.mock import patch
from country_pricer import CountryPricer

class CoutryPricerTests(unittest.TestCase):


    def test_patch_class_helper(self):
        with patch('country_pricer.country.default', 'GB'):
            pricer = CountryPricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 80)

        pricer = CountryPricer()
        self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 100)
