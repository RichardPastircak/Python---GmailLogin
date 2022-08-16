import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Load user input and ready the URL for login
print("Application for logging in to the Gmail. Please provide your email and password.")
username = input("Enter your email: ")
password = input("Enter your password: ")

url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

#Initilize driver and open gmail.com login page
driver = None
try:
    driver = uc.Chrome(use_subprocess=True)
except:
    print("Google chrome browser missing from your computer. Please install it and try again.")
else:
    wait = WebDriverWait(driver,20)
    driver.get(url)
    driver.maximize_window()

    #Process of logging in
    wait.until(EC.visibility_of_element_located((By.ID, "identifierId"))).send_keys(username)
    wait.until(EC.visibility_of_element_located((By.ID, "identifierNext"))).click()
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)
    wait.until(EC.visibility_of_element_located((By.ID, "passwordNext"))).click()

    print("You were successfully logged in.")
    input("\nWaiting for any input to end program...")




