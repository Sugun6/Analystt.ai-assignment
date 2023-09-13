# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (in this case, for Chrome)
driver = webdriver.Chrome(executable_path='path_to_chromedriver.exe')  # Replace with the path to your Chromedriver executable

# Navigate to the login page of the sample web application
driver.get('https://example.com/login')  # Replace with the actual URL of the login page

try:
    # Find the username and password input fields by their name attribute
    username_input = driver.find_element(By.NAME, 'username')  # Replace 'username' with the actual name attribute of the username field
    password_input = driver.find_element(By.NAME, 'password')  # Replace 'password' with the actual name attribute of the password field

    # Enter your login credentials
    username_input.send_keys('your_username')  # Replace 'your_username' with your actual username
    password_input.send_keys('your_password')  # Replace 'your_password' with your actual password

    # Submit the login form
    password_input.send_keys(Keys.RETURN)

    # Wait for the login process to complete (you can adjust the timeout as needed)
    WebDriverWait(driver, 10).until(EC.url_matches('https://example.com/dashboard'))  # Replace with the URL of the dashboard page

    # If the URL matches the dashboard page, the login was successful
    print('Login successful!')

except Exception as e:
    print(f'Login failed: {str(e)}')

finally:
    # Close the WebDriver
    driver.quit()
