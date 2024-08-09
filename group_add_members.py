import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Read phone numbers from CSV
def get_phone_numbers_from_csv(file_path):
    df = pd.read_csv(file_path)
    phone_numbers = df['phone_number'].tolist()  # Assuming the column name is 'phone_number'
    return phone_numbers

# Step 2: Set up Selenium WebDriver
def setup_whatsapp_web():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://web.whatsapp.com')
    print("Please scan the QR code in WhatsApp Web to log in.")
    time.sleep(20)  # Wait time for QR code scanning (adjust if necessary)
    return driver

# Step 3: Add Students to WhatsApp Group
def add_to_whatsapp_group(driver, group_name, phone_numbers):
    wait = WebDriverWait(driver, 20)

    # Search for the group
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
    search_box.click()
    search_box.send_keys(group_name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Open group settings to add participants
    menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="menu"]')))
    menu_button.click()
    time.sleep(1)

    add_participants_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Add members"]')))
    add_participants_button.click()
    time.sleep(2)

    # Add all phone numbers to the search box
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
    for number in phone_numbers:
        search_box.send_keys(number)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)
    
    # Locate and click the Confirm button
    try:
        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-animate-btn="true"]')))
        confirm_button.click()
        print("Clicked Confirm button for all numbers")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred while trying to click the 'Confirm' button: {e}")

    # Locate and click the "Add member" button in the pop-up
    try:
        add_member_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "x889kno") and contains(., "Add member")]')))
        add_member_button.click()
        print("Clicked 'Add member' button.")
    except Exception as e:
        print(f"An error occurred while trying to click the 'Add member' button: {e}")

    # Click the final confirmation button with the checkmark icon
    try:
        final_confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@aria-label="Confirm"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", final_confirm_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", final_confirm_button)
        print("Members added successfully.")
    except Exception as e:
        print(f"An error occurred while trying to click the final 'Confirm' button: {e}")

if __name__ == "__main__":
    file_path = 'phone_number.csv'  # Path to your CSV file
    group_name = 'Group name'  # Name of the WhatsApp group

    phone_numbers = get_phone_numbers_from_csv(file_path)
    driver = setup_whatsapp_web()
    add_to_whatsapp_group(driver, group_name, phone_numbers)

    print("All students have been added to the WhatsApp group.")
