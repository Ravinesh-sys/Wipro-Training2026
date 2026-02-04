from selenium import webdriver
import time

# Step 1: Open browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Navigate to example.com
driver.get("https://example.com")
print("Page Title after opening example.com:")
print(driver.title)

time.sleep(2)

# Step 3: Navigate to another page on same site
driver.get("https://www.iana.org/domains/example")
print("\nPage Title after navigating to another page:")
print(driver.title)

time.sleep(2)

# Step 4: Navigate back
driver.back()
print("\nPage Title after back navigation:")
print(driver.title)

time.sleep(2)

# Step 5: Navigate forward
driver.forward()
print("\nPage Title after forward navigation:")
print(driver.title)

time.sleep(2)

# Step 6: Refresh the page
driver.refresh()
print("\nPage Title after refresh:")
print(driver.title)

time.sleep(2)

# Step 7: Close the browser
driver.quit()
