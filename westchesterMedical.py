
# -- Adewale Adenle -- April 18, 2024 @ 3:04 PM

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

from utils.file import WriteCsvFile



#   four headers for each sheet
#   First Name, Last Name, Email, Error
#   Error should remain blank for now


# <h2>
#       <span>
#            <string> Faculty</strong>
#      </span>
# </h2>

options = Options()
service = Service(ChromeDriverManager().install())

# Initialize the Chrome driver with the specified service and options
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.westchestermedicalcenter.org/anesthesiology-residency-program")
print(driver.title)



# Wait until the dropdown is available to ensure it's loaded
wait = WebDriverWait(driver, 10)
select_element = wait.until(EC.presence_of_element_located((By.ID, 'ui-id-4')))
print(select_element)

# Click on the selected element
select_element.click()


try:
    # Locate the h2 element by its text content
    h2_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//h2[span/strong[contains(., 'Faculty')]]")))

    for h2_element in h2_elements:
        # Now find the next sibling 'p' tags that contain the names within 'strong' tags
        # We'll assume that the 'p' tag immediately follows the h2
        p_elements = h2_element.find_elements(By.XPATH, "following-sibling::p")

        for p_element in p_elements:
            # Extract the text from 'strong' tags within 'p' tags
            strong_tags = p_element.find_elements(By.TAG_NAME, 'strong')

            for strong_tag in strong_tags:
                full_text = strong_tag.text
                # Split the text by commas to separate names and credentials
                name_parts = full_text.split(',')
                # The first part is assumed to be the name
                name = name_parts[0].strip() if name_parts else None
                    

                if name != "– WMC Anesthesiology Graduate" and name != "– WMC Anesthesiology Graduate 1974" and len(name) > 0:
                    print(f"Extracted Name: {name}")

except TimeoutException:
    print(f"Timed out waiting for the category to load. Moving to next category.") 

time.sleep(15)

driver.quit()