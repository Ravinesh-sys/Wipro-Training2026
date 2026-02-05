from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

wait = WebDriverWait(driver, 20)

# Fill form
driver.find_element(By.ID, "firstName").send_keys("Ravinesh")
driver.find_element(By.ID, "lastName").send_keys("Tiwari")
driver.find_element(By.ID, "userEmail").send_keys("ravinesh@gmail.com")
driver.find_element(By.ID, "userNumber").send_keys("9876543210")  # compulsory

#Select gender
driver.find_element(By.XPATH, "//label[text()='Male']").click()

#Select hobby
driver.find_element(By.XPATH, "//label[text()='Sports']").click()
#Scroll
driver.execute_script("window.scrollTo(0,800)")
time.sleep(2)

#State
state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("NCR")
state.send_keys("\n")

#City
city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Delhi")
city.send_keys("\n")

time.sleep(2)

#Submit form
submit = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView();", submit)
time.sleep(1)
driver.execute_script("arguments[0].click();", submit)

#Wait for confirmation
confirmation = wait.until(
    EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
).text

if "Thanks" in confirmation:
    print("Form submitted successfully ✅")
else:
    print("Submission failed ❌")

time.sleep(5)
driver.quit()
