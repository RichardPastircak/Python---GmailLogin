import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


loged_in = True
print("Application for logging in to the Gmail. Please provide your email and password.")
url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver = None

#Load user input
while (loged_in):
    username = input("Enter your email: ")
    password = input("Enter your password: ")

    #Initilize driver if Chrome browser present and open gmail.com login page
    try:
        driver = uc.Chrome(use_subprocess=True)
    except:
        print("Google chrome browser missing from your computer. Please install it and try again.")
    else:
        wait = WebDriverWait(driver,20)
        driver.get(url)
        driver.maximize_window()

        #Try to login, if email/password are wrong repeat whole proccess
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "identifierId"))).send_keys(username)
            wait.until(EC.visibility_of_element_located((By.ID, "identifierNext"))).click()
            wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)
            wait.until(EC.visibility_of_element_located((By.ID, "passwordNext"))).click()
            wait.until(EC.visibility_of_element_located((By.ID, ":1s")))
        except:
            print("Wrong email or password. Please try again.")
            driver.close()
        else:
            loged_in = False
print("You were successfully logged in.")
input("\nWaiting for any input to end program...")




