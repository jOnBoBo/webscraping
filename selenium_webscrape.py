from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the login URL
login_url = "https://www.chesskid.com/login"

#input username/password
username = input("Type your username: ")
password = input("Type your password: ")

# Create a new instance of the Chrome webdriver
driver = webdriver.Chrome()

# Navigate to the login URL
driver.get(login_url)

# Find the username and password inputs
username_input = driver.find_element_by_id("loginusername")
password_input = driver.find_element_by_id("password")


# Enter your username and password
username_input.send_keys("avosps10")
password_input.send_keys("icnchess")

# Submit the form
password_input.send_keys(Keys.RETURN)

# Wait for the page to load
driver.implicitly_wait(10)


# Check if the user has been successfully logged in
# Define the login credentials
assert "chesskid.com/home" in driver.current_url

#Going to puzzles by redirecting website
driver.get("https://www.chesskid.com/puzzles/home")



soup = BeautifulSoup(driver.page_source,"lxml")

table = soup.find("table", {"class": "recent-puzzles-table main-table"})
if table is None:
    driver.get("https://www.chesskid.com/me/puzzle-history")
    soup.find('div',{'id':'app'})
    
    

# Extract the table header and rows using Beautiful Soup
header = []
rows = []
for i, row in enumerate(table.find_all("tr")):
    if i == 0:
        header = [cell.get_text().strip() for cell in row.find_all("th")]
    else:
        rows.append([cell.get_text().strip() for cell in row.find_all("td")])

# Create a pandas DataFrame from the table data
df = pd.DataFrame(rows, columns=header)

# Write the DataFrame to an Excel file
df.to_excel("table_data.xlsx", index=False)




#close browser
driver.close()
'''
#Going to puzzles through click actions
# maximize the window
driver.maximize_window()

#hovers on play
element = driver.find_element_by_css_selector("a[href='/play-chess']")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
#clicks on puzzles
link = driver.find_element_by_css_selector("a[href='/puzzles/home']")
link.click()

# Extract the table header
header = []
for th in table.find_all("th"):
    header.append(th.text.strip())

# Extract the table rows
rows = []
for tr in table.find_all("tr")[1:]:
    row = []
    for td in tr.find_all("td"):
        row.append(td.text.strip())
    rows.append(row)

# Print the header and rows
print(header)
print(rows)

'''