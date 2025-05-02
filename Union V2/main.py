from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=chrome_options)

# 命令行启动Chrome
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Temp\ChromeProfile"

# 定义网址列表
urls = [
]

while True:
    for url in urls:  # 新增循环遍历网址列表
        try:
            driver.delete_all_cookies()
            driver.get(url)
            driver.execute_script("window.location.reload(true);")
            time.sleep(5)

            transfer_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Transfer ready')]")
            transfer_button.click()
            time.sleep(3)

            while True:
                sumbit_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Submit')]")
                retry_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Retry')]")

                if sumbit_buttons:
                    sumbit_buttons[0].click()
                    print("点击 'Submit' 按钮")
                    time.sleep(5)
                    break
                elif retry_buttons:
                    retry_buttons[0].click()
                    print("检测到 'Submit' 失败，点击 'Retry' 重新尝试")
                    time.sleep(5)
                else:
                    print("等待 'Submit' 按钮出现...")
                    time.sleep(3)

            time.sleep(10)

        except Exception as e:
            print(f"处理 {url} 时发生错误: {e}")
            time.sleep(5)