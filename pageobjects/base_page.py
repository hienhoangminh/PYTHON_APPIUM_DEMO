from appium import webdriver
from time import sleep
import random
import string
import names
# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element_by_id(self, *locator):
        return self.driver.find_element_by_id(*locator)

    def get_element_by_acc_id(self, *locator):
        return self.driver.find_element_by_accessibility_id(*locator)

    def click_element_by_id(self,locator):
        el = self.get_element_by_id(locator)
        el.click()

    def click_element_by_acc_id(self,locator):
        el = self.get_element_by_acc_id(locator)
        el.click()

    def input_element_by_id(self,value,locator):
        el = self.get_element_by_id(locator)
        el.send_keys(value)

    def assert_text(self,value,locator):
        el = self.get_element_by_id(locator)
        assert el.text == value

    def wait_for_sec(self,second):
        sleep(second)

    def clear_element_content(self,locator):
        el = self.get_element_by_id(locator)
        el.clear()

    def switch_app(self,appPackage,appActivity):
        self.driver.start_activity(appPackage,appActivity)

    def get_elements_by_xpath(self,locator):
        els = self.driver.find_elements_by_xpath(locator)
        return els

    def get_index_of_element(self,locator,value):
        els = self.get_elements_by_xpath()
        i = 0
        while i < len(els):
            if els[i] == value:
                break
                return i
            else:
                i += 1

    def get_text_element_with_idx(self,locator,index):
        return self.find_element_by_xpath(locator)[index].text

