
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, time=10, poll=0.5):
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, time=10, poll=0.5):
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        self.find_element(loc).click()

    def input_element(self, loc, text):
        input_ele = self.find_element(loc)
        input_ele.clear()
        input_ele.send_keys(text)

    def get_content_element(self, loc, position):
        return self.find_elements(loc)[position].get_attribute("text")
        # first_con = self.find_elements(loc)[0]
        # return first_con.text()

    def sys_key_event(self, key_code):
        self.driver.keyevent(key_code)

    def swipe(self, x1, y1, x2, y2):
        self.driver.swipe(x1, y1, x2, y2, 1000)



