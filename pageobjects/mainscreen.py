from pageobjects.base_page import Page
from pageobjects.settingscreen import SettingScreen
from locators import locators


class MainScreen(Page):

    def click_searchBox(self):
        self.click_element_by_id(locators.SEARCH_BOX)

    def input_deptAddr(self, value):
        self.input_element_by_id(value, locators.DEPARTURE_ADR)

    def click_suggestedAddr(self, second):
        self.wait_for_sec(second)
        self.click_element_by_id(locators.SUGGESTED_ADDR)

    def input_arrAddr(self, value):
        self.input_element_by_id(value, locators.ARRIVAL_ADDR)

    def click_note(self):
        self.click_element_by_id(locators.BTN_NOTE)

    def input_note(self, value):
        self.input_element_by_id(value, locators.NOTE_FIELD)

    def save_note(self):
        self.click_element_by_id(locators.BTN_SAVENOTE)

    def click_back(self):
        self.click_element_by_id(locators.BTN_BACK)

    def click_hamburger_menu(self):
        self.click_element_by_acc_id(locators.HAM_MENU)
        return SettingScreen(self.driver)