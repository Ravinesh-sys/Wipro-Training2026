from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# open website
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

#Trigger simple alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(2)

alert = driver.switch_to.alert
print("Alert message:", alert.text)

# Accept alert
alert.accept()
print("Simple alert accepted")
time.sleep(2)

# Confirmation alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(2)

confirm_alert = driver.switch_to.alert
print("Confirm message:", confirm_alert.text)

confirm_alert.dismiss()   # dismiss
print("Confirmation alert dismissed")
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(2)

prompt = driver.switch_to.alert
print("Prompt message:", prompt.text)

prompt.send_keys("Hello Rahul")   # enter text
prompt.accept()
print("Text entered and accepted")
time.sleep(2)

# Verify result
result = driver.find_element(By.ID, "result").text
print("Result on page:", result)

time.sleep(5)
driver.quit()
