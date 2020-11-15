from selenium.webdriver.common.by import By

"""
    微信主页
"""
# 发现朋友圈按钮
find_btn = (By.XPATH, "//*contains(@text, '发现')")
# 进入朋友圈按钮
Moments_btn = (By.XPATH, "//*[@resource-id='android:id/title'][@text='朋友圈']")
# Moments_btn = (By.XPATH, "//*contains(@text, '朋友圈')")

"""
    朋友圈列表
"""
# 第一条朋友圈
First_moment = (By.ID, "com.tencent.mm:id/b_l")
# 朋友圈的发送者
pyq_name = (By.ID, "com.tencent.mm:id/e3x")

"""
    微信搜索页面
"""
# 主页搜索按钮
search_buttonHome = (By.ID, "com.tencent.mm:id/f8y")
# 通讯录与发现页面搜索按钮
search_button = (By.ID, "com.tencent.mm:id/cn1")


# 搜索输入框
search_text = (By.ID, "com.tencent.mm:id/bhn")
# 搜索结果
search_result = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/gbv'][@text='狗蛋']")

"""
    微信聊天页面
"""
# 信息输入框
sms_text = (By.ID, "com.tencent.mm:id/al_")
# 发送按钮
send_button = (By.ID, "com.tencent.mm:id/anv")
