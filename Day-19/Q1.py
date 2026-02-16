from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# open browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.maximize_window()


# IMPLICIT WAIT
driver.implicitly_wait(10)
print("Implicit wait applied (10 seconds)")

# login first
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# EXPLICIT WAIT
# wait until Add to cart clickable

try:
    wait = WebDriverWait(driver, 15)
    add_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    print("Explicit wait successful - element clickable")
    add_btn.click()

except:
    print("Explicit wait failed")
