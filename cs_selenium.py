from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
url='https://www.baidu.com'
browser.get(url)
js = f'window.open("{url}");'
print(js)
browser.execute_script(js)

print(browser.current_window_handle)  # 输出当前窗口句柄（百度）
handles = browser.window_handles
print(handles)
for handle in handles:
    if handle != browser.current_window_handle:
        print('switch to ', handle)
        browser.switch_to_window(handle)
        print(browser.current_window_handle)
        break

# browser.close()
# browser.switch_to_window(handles[0])
# import time
# time.sleep(10)
# browser.quit()