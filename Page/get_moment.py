import time
import Page
from Base.Base import Base


class Get_moment(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_moment(self):
        time.sleep(5)
        self.swipe(1020, 1258, 216, 1258)

        self.swipe(1020, 1258, 216, 1258)
        # # 点击发现
        # self.click_element(Page.find_btn)
        # 点击朋友圈
        self.click_element(Page.Moments_btn)
        # 获取第一条朋友圈内容
        massage = self.get_content_element(Page.First_moment)
        # 返回
        self.back_parent()
        return massage
