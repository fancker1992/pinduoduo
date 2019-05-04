from appium import webdriver


def init_driver():
    # 前置代码
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.taobao.taobao'
    desired_caps['appActivity'] = 'com.taobao.tao.TBMainActivity'
    # 中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
