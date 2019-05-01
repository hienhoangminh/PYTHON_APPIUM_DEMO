#coding=utf-8

import time
import unittest

from drivers import AppiumDriver
from pageobjects.mainscreen import MainScreen
from pageobjects.settingscreen import SettingScreen
from pageobjects.splashscreen import SplashScreen
from appium import webdriver
from locators import locators


class TestAppBe(unittest.TestCase):

    booking_page = None
    setting_page = None

    def setUp(self):
        self.driver = AppiumDriver.Driver().get_driver()

    def test_booking(self):
        booking_page = MainScreen(self.driver)
        booking_page.click_searchBox()
        booking_page.input_deptAddr("117 Lý Chính Thắng, phường 7, quận 3, Hồ Chí Minh")
        booking_page.click_suggestedAddr(2)
        booking_page.input_arrAddr("108 Nguyễn Đình Chiểu, phường 6, quận 3, Hồ Chí Minh")
        booking_page.click_suggestedAddr(3)
        booking_page.click_note()
        booking_page.input_note('Test the note')
        booking_page.save_note()
        booking_page.click_back()

        # When click on the hamburger menu, we instantiate SettingScreen
        setting_page = booking_page.click_hamburger_menu()
        setting_page.click_arrow_nav()
        setting_page.click_edit_profile()
        setting_page.input_nw_uname(15)
        setting_page.click_save_nwname()
        setting_page.click_logout()
        setting_page.click_confirm_logout()

    def tearDown(self):
        AppiumDriver.Driver().quit_driver()

    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(BeTestCases)
        unittest.TextTestRunner(verbosity=2).run(suite)
