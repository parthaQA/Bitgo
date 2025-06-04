from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

import time


class Main_Page:
    text = (By.CSS_SELECTOR, ".transactions h3")
    txn_txt = (By.CLASS_NAME, "transaction-box")
    one_input_two_outputs = (By.CSS_SELECTOR, ".input:nth-child(1) + .output:nth-child(2)")
    two_inputs = (By.XPATH, "//div[@class='vouts']")
    one_input = (By.XPATH, "//div[@class='vins']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20, ignored_exceptions=[
            StaleElementReferenceException])

    def validate_page_title(self, expected_title: str):
        expected_title = self.driver.title
        return self.wait.until(EC.title_is(expected_title))

    def validate_text(self):
        element = self.wait.until(EC.presence_of_element_located(self.text))
        return element.text

    def get_transactions_count(self):
        elements = self.wait.until(EC.presence_of_all_elements_located(self.txn_txt))
        return len(elements)

    def get_transaction_for_one_input_and_two_outputs(self):
        list1 = []
        elements = self.wait.until(EC.presence_of_all_elements_located(self.two_inputs))
        for element in elements:
            el = element.find_elements(By.CLASS_NAME, "vout")
            if len(el)<=2:
                for ele in el:
                    list1.append(ele.text)

        print(list1)
        print(len(list1))

        list2 = []
        elements2 = self.wait.until(EC.presence_of_all_elements_located(self.one_input))
        for element1 in elements2:
            el1 = element1.find_elements(By.CLASS_NAME, "vin")
            if len(el1) <= 1:
                for ele in el1:
                    list2.append(ele.text)

        print(list2)
        print(len(list2))


