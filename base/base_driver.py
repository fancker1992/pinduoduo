from appium import webdriver


def init_driver():
    # 前置代码
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.yiwang'
    desired_caps['appActivity'] = 'com.yiwang.HomeActivity'
    # desired_caps['appPackage'] = 'com.ddsy.songyao'
    # desired_caps['appActivity'] = '.activity.MainActivity'
    # desired_caps['appPackage'] = 'com.tencent.mm'
    # desired_caps['appActivity'] = '.ui.LauncherUI'
    # 中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 免重置
    desired_caps['noReset'] = True
    # toast
    # desired_caps['automationName'] = 'Uiautomator2'

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
