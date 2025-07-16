import unittest
import os
import time
from models.sweet import Sweet
from services.add_sweet import AddSweetService
from services.search_sweets import SearchSweetService

class TestSearchSweets(unittest.TestCase):

    def setUp(self):
        self.test_db_name = "test_sweetshop.db"
        self.adder = AddSweetService(db_name=self.test_db_name)
        self.searcher = SearchSweetService(db_name=self.test_db_name)

        # Seed sweets
        self.adder.add_sweet(Sweet(id=5001, name="Barfi", category="Milk-Based", price=20.0, quantity=10))
        self.adder.add_sweet(Sweet(id=5002, name="Gulab Jamun", category="Milk-Based", price=30.0, quantity=15))
        self.adder.add_sweet(Sweet(id=5003, name="Candy Pop", category="Candy", price=5.0, quantity=50))
        self.adder.add_sweet(Sweet(id=5004, name="Dark Chocolate", category="Chocolate", price=50.0, quantity=25))

    def tearDown(self):
        self.adder.db.close_connection()
        self.searcher.db.close_connection()
        time.sleep(0.1)
        if os.path.exists(self.test_db_name):
            os.remove(self.test_db_name)

    def test_search_by_name(self):
        result = self.searcher.search_sweets(name="barfi")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Barfi")

    def test_search_by_category(self):
        """
        Test that sweets can be searched by exact category.
        """
        result = self.searcher.search_sweets(category="Milk-Based")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(s.category == "Milk-Based" for s in result))

    def test_search_by_name_case_insensitive(self):
        """
        Test that name search is case-insensitive.
        'barfi' should match 'Barfi' in DB.
        """
        result = self.searcher.search_sweets(name="BaRfI")  # Mixed case
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Barfi")

    def test_search_by_price_range(self):
        """
        Test that sweets can be filtered within a price range.
        """
        result = self.searcher.search_sweets(min_price=10.0, max_price=30.0)

        self.assertEqual(len(result), 2)  # Should return Barfi (20), Gulab Jamun (30)

        for sweet in result:
            self.assertGreaterEqual(sweet.price, 10.0)
            self.assertLessEqual(sweet.price, 30.0)

    def test_invalid_search_inputs(self):
        """
        Test that invalid search filters return an empty list and do not crash.
        """
        result1 = self.searcher.search_sweets(name=123)  # name must be str
        result2 = self.searcher.search_sweets(category=[])  # category must be str
        result3 = self.searcher.search_sweets(min_price="cheap")  # min_price must be float/int
        result4 = self.searcher.search_sweets(max_price="expensive")  # max_price must be float/int

        self.assertEqual(result1, [])
        self.assertEqual(result2, [])
        self.assertEqual(result3, [])
        self.assertEqual(result4, [])

    def test_search_with_no_filters_returns_all(self):
        """
        Test that all sweets are returned when no filters are provided.
        """
        result = self.searcher.search_sweets()
        self.assertEqual(len(result), 4)  # setUp added 4 sweets
        names = sorted([s.name for s in result])
        expected_names = sorted(["Barfi", "Gulab Jamun", "Candy Pop", "Dark Chocolate"])
        self.assertEqual(names, expected_names)

    def test_search_with_partial_price_filters(self):
        """
        Test that search works with only min_price or only max_price.
        """
        result_min = self.searcher.search_sweets(min_price=25)
        self.assertTrue(all(s.price >= 25 for s in result_min))
        
        result_max = self.searcher.search_sweets(max_price=15)
        self.assertTrue(all(s.price <= 15 for s in result_max))

    def test_search_with_combined_filters(self):
        """
        Test search with name + category + price range combined.
        Should match 'Gulab Jamun' (Milk-Based, 30.0).
        """
        result = self.searcher.search_sweets(
            name="gulab",
            category="Milk-Based",
            min_price=20,
            max_price=35
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Gulab Jamun")