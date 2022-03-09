import unittest
from amazon_store_handler import *

# Invalid Credentials
invalid_username = "test@test.com"
invalid_password = "invalidpassword"


class MyTestCase(unittest.TestCase):
    amazon_store_handler = None

    @classmethod
    def setUpClass(cls):
        cls.amazon_store_handler = AmazonStoreHandler(headless=False)
        return

    def test_amazon_search(self):
        print("Step 1: Navigate To The Login Page...")
        self.amazon_store_handler.navigate_to_login()
        print("success")

        print("Step 2: Enter Invalid Credentials...")
        self.amazon_store_handler.enter_login_credentials(invalid_username, invalid_password)
        login_error_header, login_error_message = self.amazon_store_handler.get_login_error_message()
        self.assertEqual(login_error_header, "There was a problem")
        self.assertEqual(login_error_message, "Your password is incorrect")
        print("success")
        return

    @classmethod
    def tearDownClass(cls):
        return


if __name__ == '__main__':
    unittest.main()
