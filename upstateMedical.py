# -- Adewale Adenle -- April 18, 2024 @ 6:15 PM

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.file import WriteCsvFile
import time


#   REQUIREMENTS
#   four headers for each sheet
#   First Name, Last Name, Email, Error
#   Error should remain blank for now



options = Options()
service = Service(ChromeDriverManager().install())

# Initialize the Chrome driver with the specified service and options
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.upstate.edu/anesthesiology/about-us/faculty.php")
print(driver.title)

wait = WebDriverWait(driver, 10)

department = ["Department Chair", "Vice-Chair of Education", "Vice-Chair of Academic Innovation", "Vice-Chair of Quality Assurance"]
try:
    # Find the h2 element that contains the text "Department Chair"
    for dept in department:
        department_chair_h2 = wait.until(EC.presence_of_element_located((By.XPATH, f"//h2[contains(text(), '{dept}')]")))
        # Find the <p> element that directly follows the <h2>
        department_chair_p = department_chair_h2.find_element(By.XPATH, "./following-sibling::p")

        # Within the <p> element, find the <a> tag and extract the text
        department_chair_link = department_chair_p.find_element(By.TAG_NAME, "a")
        full_name = department_chair_link.text.strip()

        # Assuming the full name is in the format "First Last", split the string
        first_name, last_name = full_name.split(' ', 1)

        # Now you have the first and last name and can do what you need with it
        print(f"First Name: {first_name}, Last Name: {last_name}")


    # Now you have the h2 element and can do what you need with it
    # print(department_chair_h2.text)

except Exception as e:
    print("Couldn't find an h2 element with the text")

titles = ["Professor", "Associate Professor", "Assistant Professor", "Clinical Assistant Professor","Instructor", "Nurse Practitioner"]
try:
    for title in titles:
        title_h2 = wait.until(EC.presence_of_element_located((By.XPATH, f"//h2[contains(text(), '{title}')]")))
        title_div = title_h2.find_element(By.XPATH, "following-sibling::div")

        
        title_ul = title_div.find_element(By.TAG_NAME, "ul")

        
        title_li = title_ul.find_elements(By.TAG_NAME, "li")
        for li in title_li:
            title_link = li.find_element(By.TAG_NAME, "a")

            full_name = title_link.text.split(',')[0].strip()
            first_name, last_name = full_name.split(' ', 1)
            # print(f"First Name: {first_name}, Last Name: {last_name}")
            
            # Create an instance of the class
            csv_writer = WriteCsvFile("Upstate_Medical.csv", first_name, last_name, '', '')

            # Write to the CSV file
            csv_writer.write_csv_file()

            

except Exception as e:
    print("Couldn't find an h2 element with the text ")

time.sleep(15)

driver.quit()


