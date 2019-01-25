from appium import webdriver
import time
import allure
import pytest


class Test_loc:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = ''
        desired_caps['deviceName'] = 'sanxing'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    def teardown_class(self):
        self.driver.quit()
    @allure.step(title="进入修改界面")
    @pytest.fixture(scope='class',autouse=True)
    def goin_loc(self):
        save = self.driver.find_element_by_xpath("//*[contains(@text,'存储')]")
        more = self.driver.find_element_by_xpath("//*[contains(@text,'更多')]")
        self.driver.drag_and_drop(save, more)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(@text,'位置信息')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(@text,'模式')]").click()
        time.sleep(5)
    @allure.step(title="进行模式修改")
    def test_loc(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'使用GPS、WLAN和移动网络确定位置')]").click()
        time.sleep(2)
        self.driver.find_element_by_class_name('android.widget.ImageButton').click()
        time.sleep(2)
        res = self.driver.find_elements_by_id('android:id/summary')
        assert '准确度高' in [i.text for i in res]





