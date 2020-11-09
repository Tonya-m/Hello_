from Base.Init_Driver import Init_Driver
from Page.get_moment import Get_moment
from Page.send_sms import Send_sms


class TestSendMoment():
    def __init__(self):
        self.driver = Init_Driver()

    def test_SendMent(self):
        message = Get_moment(self.driver)
        ss = Send_sms(self.driver)
        ss.send_message("狗蛋", message.get_moment())
        self.driver.quit()


if __name__ == '__main__':
    TestSendMoment().test_SendMent()