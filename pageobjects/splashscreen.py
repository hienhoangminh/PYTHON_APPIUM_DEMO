from pageobjects.base_page import Page
from locators import locators

class SplashScreen(Page):

    def input_phone_number(self,value):
        self.input_element_by_id(value,locators.PHONE_NO_FIELD)

    def click_next(self):
        self.click_element_by_id(locators.BTN_NEXT)

    def get_otp_code(self):
        self.switch_app("com.samsung.android.messaging","com.android.mms.ui.ConversationComposer")
        self.wait_for_sec(2)

        self.click_element_by_id(locators.BTN_BACK_MESS)

        idx = self.get_index_of_element(locators.FROM_MESSAGE,'BE GROUP')
        otp_message = self.get_text_element_with_idx(locators.CONTENT_MESSAGE,idx)
        print(otp_message)






