import string
from random import choice

from pageobjects.base_page import Page
from locators import locators

class SettingScreen(Page):

    def click_arrow_nav(self):
        self.click_element_by_id(locators.NAV_ARROW)

    def click_edit_profile(self):
        self.click_element_by_id(locators.BTN_EDIT_PROFILE)

    def input_nw_uname(self,length=10):
        value = ''.join([choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(length)])
        self.clear_element_content(locators.FIELD_UNAME)
        self.input_element_by_id(value,locators.FIELD_UNAME)

    def click_save_nwname(self):
        self.click_element_by_id(locators.BTN_SUBMIT)

    def click_logout(self):
        self.click_element_by_id(locators.BTN_LOGOUT)

    def click_confirm_logout(self):
        self.click_element_by_id(locators.BTN_LOGOUT_CONFIRM)