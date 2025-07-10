from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  # hoặc thêm đường dẫn vào chromedriver nếu cần
driver.get("https://demo.nopcommerce.com/login")

driver.find_element(By.ID, "Email").send_keys("test@example.com")
driver.find_element(By.ID, "Password").send_keys("123456")
driver.find_element(By.CLASS_NAME, "login-button").click()

time.sleep(2)
print("Page title:", driver.title)

driver.quit()
