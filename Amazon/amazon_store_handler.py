import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

DRIVER_PATH = "Amazon/ChromeDriver/chromedriver"
AMAZON_URL = "http://www.amazon.com/"
WAIT_TIMEOUT = 10

# Element Identifier Constants
SEARCH_BAR_ID = "twotabsearchtextbox"
RESULT_LIST_CLASS_NAME = "s-main-slot.s-result-list"
SIGNUP_BUTTON_ID = "nav-signin-tooltip"
EMAIL_FIELD_NAME = "email"
PASSWORD_FIELD_NAME = "password"
LOGIN_ERROR_MESSAGE_BOX_ID = "auth-error-message-box"
SHOPPING_CART_BUTTON_ID = "nav-cart"
SHOPPING_CART_ID = "sc-active-cart"
SHOPPING_CART_ITEM_ID = "sc-list-item"
SEARCH_RESULT_PRICE_CLASS_NAME = "a-price"
SEARCH_RESULT_PAGE_CLASS_NAME = "s-pagination-strip"
SEARCH_RESULTS_XPATH = '//div[@data-component-type="s-search-result"]'
SEARCH_RESULT_INFO_BAR = '//span[@data-component-type="s-result-info-bar"]'
ADD_TO_CART_BUTTON_ID = "add-to-cart-button"
ADDED_TO_CART_TEXT_CLASS_NAME = "sw-atc-text"
PRODUCT_PAGE_PRODUCT_TITLE_ID = "productTitle"


class AmazonStoreHandler(object):

    def __init__(self, driver_path=DRIVER_PATH):
        # Initializes Web Browser
        chrome_options = webdriver.ChromeOptions()

        self.service = Service(driver_path)
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url, options=chrome_options)
        self.web_driver_wait = WebDriverWait(self.driver, WAIT_TIMEOUT)

        # Start The Window Full-Screen
        self.driver.maximize_window()

        # Clear Cookies
        self.driver.delete_all_cookies()

        # Opens The Amazon Store Page
        self.driver.get(AMAZON_URL)

        # Waits For Search Bar To Load
        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.ID, SEARCH_BAR_ID)))
        return

    def __del__(self):
        if self.driver:
            self.driver.quit()
        return

    @staticmethod
    def type_text(text_field_element, text_value, hit_enter=True):
        text_field_element.clear()
        text_field_element.send_keys(text_value)
        if hit_enter:
            text_field_element.send_keys(Keys.RETURN)
        return

    def search_store(self, search_term):
        # Waits For Search Bar To Load
        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.ID, SEARCH_BAR_ID)))

        # Enter In Search Value
        search_bar_element = self.driver.find_element(By.ID, SEARCH_BAR_ID)
        self.type_text(search_bar_element, search_term)

        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,
                                                                                      RESULT_LIST_CLASS_NAME)))
        return

    def get_search_results(self):
        results = []

        self.web_driver_wait.until(expected_conditions.
                                   visibility_of_element_located((By.CLASS_NAME, SEARCH_RESULT_PAGE_CLASS_NAME)))

        elements = self.driver.find_elements(By.XPATH, SEARCH_RESULTS_XPATH)

        for element in elements:
            if "AdHolder" not in element.get_attribute("class"):
                title = element.find_element(By.TAG_NAME, "h2")
                title = title.text
                results.append(title)

        return results

    def navigate_to_login(self):
        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.ID, SIGNUP_BUTTON_ID)))
        login_button = self.driver.find_element(By.ID, SIGNUP_BUTTON_ID)
        login_button.click()
        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.NAME, EMAIL_FIELD_NAME)))
        return

    def enter_login_credentials(self, username, password):
        # Verify The Email Field Is Visibile
        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.NAME, EMAIL_FIELD_NAME)))

        # Enter Username
        username_field_element = self.driver.find_element(By.NAME, EMAIL_FIELD_NAME)
        self.type_text(username_field_element, username)

        # Verify The Password Field Is Visibile
        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.NAME, PASSWORD_FIELD_NAME)))
        password_field_element = self.driver.find_element(By.NAME, PASSWORD_FIELD_NAME)
        self.type_text(password_field_element, password)
        return

    def get_login_error_message(self):
        error_message_header = ""
        error_message = ""

        self.web_driver_wait.until(expected_conditions.visibility_of_element_located(
            (By.ID, LOGIN_ERROR_MESSAGE_BOX_ID)))
        password_field_element = self.driver.find_element(By.ID, LOGIN_ERROR_MESSAGE_BOX_ID)

        # Get Error Message Text
        try:
            # Get Error Message Headers
            error_message_header_element = password_field_element.find_element(By.TAG_NAME, "h4")
            error_message_element = password_field_element.find_element(By.TAG_NAME, "span")

            # Set Return Values If Both Elements Are Found
            error_message_header = error_message_header_element.text
            error_message = error_message_element.text
        except NoSuchElementException:
            pass

        return error_message_header, error_message

    def navigate_to_cart(self):
        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.ID, SHOPPING_CART_BUTTON_ID)))
        cart_button = self.driver.find_element(By.ID, SHOPPING_CART_BUTTON_ID)
        cart_button.click()

        # Wait For The Cart To Load
        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.ID, SHOPPING_CART_ID)))
        return

    def add_item_to_cart_from_search(self, item_index):
        self.web_driver_wait.until(expected_conditions.
                                   visibility_of_element_located((By.CLASS_NAME, "s-pagination-strip")))

        elements = self.driver.find_elements(By.XPATH, SEARCH_RESULTS_XPATH)
        search_results = []
        for element in elements:
            if "AdHolder" not in element.get_attribute("class"):
                search_results.append(element)
        desired_product = search_results[item_index]

        product_name = desired_product.find_element(By.TAG_NAME, "h2")
        product_name = product_name.find_element(By.TAG_NAME, "a")
        product_name.click()

        # Wait For The Page To Load
        self.web_driver_wait.until(expected_conditions.
                                   visibility_of_element_located((By.ID, PRODUCT_PAGE_PRODUCT_TITLE_ID)))

        # Wait For Add To Cart Button To Appear
        self.web_driver_wait.until(expected_conditions.
                                   visibility_of_element_located((By.ID, ADD_TO_CART_BUTTON_ID)))

        # Click Add To Cart
        add_to_cart_button = self.driver.find_element(By.ID, ADD_TO_CART_BUTTON_ID)
        add_to_cart_button.click()

        # Wait For Added To Cart Text To Appear
        self.web_driver_wait.until(expected_conditions.
                                   visibility_of_element_located((By.CLASS_NAME, ADDED_TO_CART_TEXT_CLASS_NAME)))
        return

    def get_number_of_items_in_cart(self):
        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.ID, SHOPPING_CART_ID)))

        # Get Items In Shopping Cart
        active_cart_element = self.driver.find_element(By.ID, SHOPPING_CART_ID)
        cart_item_elements = active_cart_element.find_elements(By.CLASS_NAME, SHOPPING_CART_ITEM_ID)

        return len(cart_item_elements)

    def get_items_in_cart(self):
        items_in_cart = []

        self.web_driver_wait.until(expected_conditions.visibility_of_element_located((By.ID, SHOPPING_CART_ID)))

        # Get Items In Shopping Cart
        active_cart_element = self.driver.find_element(By.ID, SHOPPING_CART_ID)
        cart_item_elements = active_cart_element.find_elements(By.CLASS_NAME, SHOPPING_CART_ITEM_ID)

        for item in cart_item_elements:
            try:
                # Find Both Elements
                title = item.find_element(By.CLASS_NAME, "a-truncate-cut")
                price = item.find_element(By.CLASS_NAME, "sc-price")

                # Grab Values And Append To List
                title = title.text
                price = price.text
                items_in_cart.append([title, price])
            except NoSuchElementException:
                pass

        return items_in_cart

    def get_number_search_results_from_item_range(self):
        expected_search_results = 0

        self.web_driver_wait.until(expected_conditions.
                                   visibility_of_element_located((By.CLASS_NAME, SEARCH_RESULT_PAGE_CLASS_NAME)))

        # Find The Element Containing The Range Of Search Results
        search_range_element = self.driver.find_element(By.XPATH, SEARCH_RESULT_INFO_BAR)
        search_range_element = search_range_element.find_element(By.TAG_NAME, "h1")

        # Pull Range From Element Text
        result_range_pattern = re.compile('(\d+)-(\d+)')
        results = result_range_pattern.findall(search_range_element.text)
        if results and results[0]:
            beginning = int(results[0][0])
            end = int(results[0][1])
            expected_search_results = end - beginning + 1

        return expected_search_results