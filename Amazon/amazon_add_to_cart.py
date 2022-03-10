import unittest
from amazon_store_handler import *


class AmazonAddToCart(unittest.TestCase):
    amazon_store_handler = None

    @classmethod
    def setUpClass(cls):
        cls.amazon_store_handler = AmazonStoreHandler(headless=False)
        return

    def test_amazon_search(self):
        search_result_item_index = 0

        print("Step 1: Verify Cart Is Empty...")
        self.amazon_store_handler.navigate_to_cart()
        self.assertEqual(self.amazon_store_handler.get_number_of_items_in_cart(), 0)
        print("success")

        print("Step 2: Search Amazon Store...")
        self.amazon_store_handler.search_store("amphibia poster")
        search_results = self.amazon_store_handler.get_search_results()
        print("success")

        print("Step 3: Add Item To Cart...")
        self.amazon_store_handler.add_item_to_cart_from_search(search_result_item_index)
        print("success")

        print("Step 3: Verify Cart Contains The Expected Item...")
        self.amazon_store_handler.navigate_to_cart()
        self.assertEqual(self.amazon_store_handler.get_number_of_items_in_cart(), 1)
        items_in_cart = self.amazon_store_handler.get_items_in_cart()
        self.assertEqual(items_in_cart[0], search_results[search_result_item_index])
        print("success")
        return

    @classmethod
    def tearDownClass(cls):
        return


if __name__ == '__main__':
    unittest.main()
