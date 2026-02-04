from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/text-box")

wait = WebDriverWait(driver, 15)

# 1️⃣ ID – Full Name
full_name = wait.until(EC.presence_of_element_located((By.ID, "userName")))
full_name.send_keys("Ravinesh Kumar")

# 2️⃣ ID – Email
email = wait.until(EC.presence_of_element_located((By.ID, "userEmail")))
email.send_keys("ravinesh@gmail.com")

# 3️⃣ CSS – Current Address
current_address = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#currentAddress"))
)
current_address.send_keys("Bangalore")

# 4️⃣ ID (shown as CLASS concept in explanation) – Permanent Address
permanent_address = wait.until(
    EC.presence_of_element_located((By.ID, "permanentAddress"))
)
permanent_address.send_keys("India")

# 5️⃣ XPATH – Submit Button (SAFE WAY)
submit_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='submit']"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
submit_btn.click()


output_name = wait.until(
    EC.presence_of_element_located((By.ID, "name"))
).text

if "Ravinesh Kumar" in output_name:
    print("✅ Validation successful: Name is displayed")
else:
    print("❌ Validation failed")

time.sleep(3)
driver.quit()
