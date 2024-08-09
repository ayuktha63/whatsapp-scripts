from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Load phone numbers from CSV file
def load_phone_numbers(file_path):
    df = pd.read_csv(file_path)
    return df['phone_number'].tolist()

# Send WhatsApp message
def send_whatsapp_message(driver, phone_number, message):
    # Navigate to WhatsApp web
    driver.get(f'https://web.whatsapp.com/send?phone={phone_number}')
    time.sleep(15)  # Wait for the page to load and QR code to be scanned

    try:
        # Locate the message input box
        message_box = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']")
        message_box.click()
        message_box.send_keys(message)
        
        # Locate and click the send button
        send_button = driver.find_element(By.CSS_SELECTOR, "button[data-tab='11']")
        send_button.click()
        time.sleep(5)  # Wait for the message to send
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Configuration
    csv_file_path = 'phone_number.csv'  # Path to your CSV file
    message = """Hello! This is a test message from the Python script.
                """  # Your message

    # Set up WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Load phone numbers
    phone_numbers = load_phone_numbers(csv_file_path)

    # Send messages
    for phone_number in phone_numbers:
        send_whatsapp_message(driver, phone_number, message)
        time.sleep(5)  # Wait before sending the next message

    driver.quit()

if __name__ == '__main__':
    main()
