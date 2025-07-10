import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bossvn.com/login")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_login_by_phone_success(self):
        driver = self.driver
        wait = self.wait

        # Chọn tab "Ứng viên"
        # wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'_tab_content') and text()='Ứng viên']"))).click()

        # Click chọn đầu số
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ant-select-selection-item"))).click()
        
        # Nhập 86 vào input tìm kiếm
        search_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ant-select-selection-search-input")))
        search_input.send_keys("86")
        
        # Chờ hiện và click vào +86
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'ant-select-item-option') and contains(., '+86')]"))
        ).click()

        # Nhập số điện thoại
        phone_input = driver.find_element(By.XPATH, "//input[@placeholder='Vui lòng nhập số điện thoại']")
        phone_input.send_keys("19900000002")

        # Click gửi mã xác thực
        send_code_btn = driver.find_element(By.XPATH, "//span[contains(text(),'Gửi mã xác thực')]")
        send_code_btn.click()

        # Nhập mã xác thực (giả lập)
        time.sleep(1)
        code_input = driver.find_element(By.XPATH, "//input[@placeholder='Vui lòng nhập mã xác nhận']")
        code_input.send_keys("6666")

        # Click xác nhận
        confirm_btn = driver.find_element(By.XPATH, "//span[text()='Xác nhận']")
        confirm_btn.click()

        # ✅ Kiểm tra điều hướng đến trang /home
        wait.until(EC.url_contains("/home"))
        self.assertIn("/home", driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="reports", report_title="Login Test Report")
    )
