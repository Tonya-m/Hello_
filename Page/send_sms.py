from Base.Base import Base
import Page

class Send_sms(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def send_message(self, name, message):
        # 点击搜索
        self.click_element(Page.search_button)
        # 输入微信名
        self.input_text(Page.search_text, name)
        # 点击微信名进入聊天界面
        self.click_element(Page.search_result)
        # 输入聊天消息
        self.input_text(Page.sms_text, message)
        # 发送消息
        self.click_element(Page.send_button)