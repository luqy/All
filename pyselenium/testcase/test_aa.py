from selenium import webdriver
def test_screenshot_on_test_failure(browser):
    #driver=webdriver.Chrome()
    browser.get("https://www.baidu.com")
    assert False
