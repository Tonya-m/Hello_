from appium import webdriver


def Init_Driver():
    # 服务端启动参数
    desired_caps = {}
    # 移动设备 系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.1'
    # 设备号
    desired_caps['deviceName'] = '8d8aca8e'
    # 包名，启动名
    desired_caps['appPackage'] = 'com.tencent.mm'
    desired_caps['appActivity'] = '.ui.LauncherUI'
    # 允许中文输入
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 避免重复安装
    desired_caps['noReset'] = True
    # 手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver