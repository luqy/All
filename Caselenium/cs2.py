from selenium import webdriver

WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
# mobileEmulation = {'deviceName': 'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
executor_url=driver.command_executor._url
session_id=driver.session_id
url='https://blog.csdn.net/huilan_same/article/details/52856200'
driver.get(url)
url='https://www.cnblogs.com/zhongyehai/p/9174620.html'
js = f'window.open("{url}");'
for i in range(2):
     driver.execute_script(js)
handle=driver.window_handles
for i in handle:
    print(i)
    driver.switch_to_window(i)



