# IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

# IMPORT CSV LIBRARY
import csv

# OPEN A NEW CSV FILE TO SAVE THE SCRAPED APPLIANCES AND PRICES
file = open('scraped_appliances_prices.csv', 'w', newline='', encoding='utf-8')
# CREATE A VARIABLE FOR WRITING TO THE CSV
writer = csv.writer(file)

# CREATE THE HEADER ROW OF THE CSV
writer.writerow(['Appliance', 'Price'])

# REQUEST THE JUMIA APPLIANCES WEBPAGE AND STORE IT AS A VARIABLE
page_to_scrape = requests.get("https://www.jumia.com.ng/mlp-appliances/")

# USE BEAUTIFULSOUP TO PARSE THE HTML CONTENT OF THE JUMIA WEBPAGE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# FIND ALL THE APPLIANCE NAMES ON THE PAGE WITH A CLASS ATTRIBUTE OF 'name'
appliances = soup.findAll("div", attrs={"class": "name"})

# FIND ALL THE APPLIANCE PRICES ON THE PAGE WITH A CLASS ATTRIBUTE OF 'prc'
prices = soup.findAll("div", attrs={"class": "prc"})

# LOOP THROUGH BOTH APPLIANCES AND PRICES USING THE 'ZIP' FUNCTION
# THEN PRINT AND FORMAT THE RESULTS
for appliance, price in zip(appliances, prices):
    print(f"{appliance.text.strip()} - {price.text.strip()}")
    # WRITE EACH APPLIANCE AND PRICE AS A NEW ROW IN THE CSV
    writer.writerow([appliance.text.strip(), price.text.strip()])

# CLOSE THE CSV FILE
file.close()
