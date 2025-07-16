import unittest
from services.sweet_shop import sweetShop
from models.sweet import Sweet


class TestSweetShop(unittest.TestCase):

    """
    Test suite for the SweetShop service class.
    All test cases follow TDD principles and validate core business logic.
    """
    
    def test_add_sweet(self):

        """
        Test that a new sweet can be successfully added to the shop.
        This is the first test in the TDD cycle.
        Edge cases and validations will be tested in later test cases.
        """
        
        shop = sweetShop()
        sweet = Sweet(id=1001, name="Kaju Katli", category="Nut-Based", price=50.0, quantity=20)
        result = shop.add_sweet(sweet)

        self.assertTrue(result)