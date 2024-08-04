from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialize the WebDriver service
home_directory = os.path.expanduser("~")
chromedriver_path = os.path.join(home_directory, "Downloads", "chromedriver-win64", "chromedriver-win64", "chromedriver.exe")
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
try:
    driver.get("https://fitpeo.com/")

    # Click on the revenue calculator link
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="/revenue-calculator"]'))
    )
    element.click()

    # Wait for the slider and input elements to be present
    slider_track = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiSlider-rail"))
    )
    slider_handle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiSlider-thumb"))
    )
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiInputBase-input"))
    )

    # Move the slider handle
    slider_range = 946
    target_value = 297
    slider_width = slider_track.size['width']
    target_position = (target_value / slider_range) * slider_width

    actions = ActionChains(driver)
    current_position = slider_handle.location['x']

    actions.click_and_hold(slider_handle).move_by_offset(target_position, 0).release().perform()
    time.sleep(3)
    # Use JavaScript to set the input field value and dispatch events
    driver.execute_script("""
        var input = document.querySelector(".MuiInputBase-input");
        input.focus();
        document.execCommand("selectAll");
        document.execCommand("delete");
        input.focus();
        document.execCommand("insertText" , true, "560");
        
    """)
    current_position = slider_handle.location['x']
    print("curr" , current_position)

    element = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

    driver.execute_script("arguments[0].scrollIntoView(true);", element[0])
    time.sleep(3)

    driver.execute_script("arguments[0].click();", element[0])
    driver.execute_script("arguments[0].click();", element[1])
    driver.execute_script("arguments[0].click();", element[2])



    # Optionally, wait and inspect the result
    time.sleep(15)

finally:
    driver.quit()


