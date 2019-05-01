from appium import webdriver

class Driver:

    def get_driver(self):
        desired_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "platformVersion": "8.1.0",
            "deviceName": "3300f3433258a34b",
            "noReset": True,
            "autoGrantPermissions": True,
            "appActivity": "SplashNewActivity",
            "appPackage": "xyz.be.customer"
        }

        self.instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        self.instance.implicitly_wait(15)
        # self.instance.reset()
        return self.instance

    def quit_driver(self):
        self.get_driver().quit()