from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # Optional: run in headless mode
driver = webdriver.Chrome(options=options)

# Function to log in to Instagram
def login(username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(random.uniform(2, 4))  # Random sleep between 2 to 4 seconds
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(random.uniform(4, 6))  # Random sleep between 4 to 6 seconds
    # Handle "Turn on Notifications" modal
    try:
        driver.find_element_by_xpath("//button[text()='Not Now']").click()
    except:
        pass

# Function to send follow requests to random users
def send_follow_requests(num_requests):
    driver.get("https://www.instagram.com/explore/people/")
    time.sleep(random.uniform(2, 4))  # Random sleep between 2 to 4 seconds
    for _ in range(num_requests):
        # Find a random user on the explore page and click to follow
        random_user = driver.find_element_by_xpath("//button[text()='Follow']")
        random_user.click()
        time.sleep(random.uniform(3, 5))  # Random sleep between 3 to 5 seconds
        print("Follow request sent")

if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    num_requests = int(input("Enter the number of follow requests to send: "))
    
    login(username, password)
    send_follow_requests(num_requests)  
    driver.quit()  # Close the WebDriver after the script finishes
