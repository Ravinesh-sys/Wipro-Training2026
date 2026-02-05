from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/register")
time.sleep(4)

print("Page title:", driver.title)

heading = driver.find_element(By.TAG_NAME,"h1").text
print("Heading:", heading)

# click register without filling
driver.find_element(By.ID,"register-button").click()
time.sleep(2)

error = driver.find_element(By.ID,"FirstName-error").text
print("Error:", error)

# fill form
driver.find_element(By.ID,"FirstName").send_keys("Ravinesh")
driver.find_element(By.ID,"LastName").send_keys("Tiwari")

email = f"ravinesh{random.randint(1000,9999)}@gmail.com"
driver.find_element(By.ID,"Email").send_keys(email)

driver.find_element(By.ID,"Password").send_keys("Ravinesh@123")
driver.find_element(By.ID,"ConfirmPassword").send_keys("Ravinesh@123")

time.sleep(2)

# submit form
driver.find_element(By.ID,"register-button").click()
print("Form submitted successfully")

time.sleep(5)
driver.quit()
