# -- Adewale Adenle -- April 18, 2024 @ 9:46 PM

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.file import WriteCsvFile


#   four headers for each sheet
#   First Name, Last Name, Email, Error
#   Error should remain blank for now


options = Options()
service = Service(ChromeDriverManager().install())

# Initialize the Chrome driver with the specified service and options
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://hsc.unm.edu/directory/")
print(driver.title)



# Wait until the dropdown is available to ensure it's loaded
wait = WebDriverWait(driver, 10)
select_element = wait.until(EC.presence_of_element_located((By.ID, 'dirDept')))


# Find the drop down  box and search for a name
select = Select(select_element)
#print out the contents of the dropdown
# for option in select.options:
#     print(option.text)

# select by value
select.select_by_visible_text('SOM - Anesthesiology')


anesthesiology_option = select_element.find_element(By.XPATH, "//option[.='SOM - Anesthesiology']")
anesthesiology_option.click()





# Extend the wait time if necessary (for example, 30 seconds)
wait = WebDriverWait(driver, 30)
print("Waiting for the 'row dirItems' elements to load")
try:
    # Wait for at least one element with the specific class name to be present
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dirItem')))

    # Find all elements with the specific class name
    dir_items = driver.find_elements(By.CLASS_NAME, 'dirItem')

    # Filter out only the elements with all the required classes
    filtered_items = [item for item in dir_items if 'col-sm-6' in item.get_attribute('class') and
                                                     'col-md-4' in item.get_attribute('class') and
                                                     'col-lg-3' in item.get_attribute('class') and
                                                     'blockImage' in item.get_attribute('class') and
                                                     'all' in item.get_attribute('class') and
                                                     'somanesthesiology' in item.get_attribute('class')]

    # Loop through the filtered elements and extract the data
    for item in filtered_items:
        first_name = item.get_attribute('data-first-name')
        last_name = item.get_attribute('data-last-name')
        # print(f"First Name: {first_name}, Last Name: {last_name}")
        WriteCsvFile('New_Mexico.csv', first_name, last_name,'', '').write_csv_file()

except Exception as e:
    print(f'Error: {e}')
    print("Timed out waiting for page to load")
    driver.save_screenshot('page_load_failure.png')


time.sleep(15)

driver.quit()