import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# path to chrome driver
chrome_driver_path = '/usr/local/bin/chromedriver'


options = webdriver.ChromeOptions()


service = Service(executable_path=chrome_driver_path)


driver = webdriver.Chrome(service=service, options=options)


url = "https://www.otipy.com/category/vegetables-1"
driver.get(url)

time.sleep(30)

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

# Create a list to store product data
products = []

# Extract product details
for product in soup.find_all('div', class_='style_card_details__qi0G9'):
    name = product.find('h3', class_='style_prod_name__QllSp').text.strip()
    
    # Extract the price section
    price_section = product.find('h6', class_='style_prod_price__4TltC')
    
    # Extract MRP
    mrp_span = price_section.find('span', class_='style_striked_price__4ghn5')
    standard_price = mrp_span.text.strip() if mrp_span else "N/A"  # This will now be the standard price
    
    # Extract selling price
    selling_price_span = price_section.find('span', class_='style_selling_price__GaIsF')
    selling_price = selling_price_span.text.strip() if selling_price_span else "N/A"
    
    # Extract final price
    final_price_section = product.find('p', class_='style_final_price__FERLK')
    final_price = final_price_section.text.strip() if final_price_section else "N/A"
    
    # Extract product quantity
    quantity = product.find('span', class_='style_prod_qt__cXcqe').text.strip()

    # Add product to the list as a dictionary
    products.append({
        'Name': name,
        'Standard Price (MRP)': standard_price,
        'Selling Price': selling_price,
        'Final Price': final_price,  # Add final price to the dictionary
        'Quantity': quantity
    })

# Saving data to a JSON file
with open('products.json', 'w') as json_file:
    json.dump(products, json_file, indent=4)


print(f"Scraped {len(products)} products and saved to products.json")
