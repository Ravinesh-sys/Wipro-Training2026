from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Firefox browser
driver = webdriver.Firefox()

# Open TutorialsNinja website
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
print("Title is:", driver.title)

# Navigate to Google
driver.get("https://www.google.com/")
print("Title is:", driver.title)

time.sleep(5)

# Navigate back
driver.back()
print("Title after back:", driver.title)

time.sleep(2)

# Navigate forward
driver.forward()
print("Title after forward:", driver.title)

time.sleep(2)

# Refresh the page
driver.refresh()
print("Title after refresh:", driver.title)

time.sleep(2)

# Close browser
driver.quit()
