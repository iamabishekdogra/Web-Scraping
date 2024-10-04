import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Path to Chrome driver
chrome_driver_path = '/usr/local/bin/chromedriver'

options = webdriver.ChromeOptions()
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.otipy.com/category/vegetables-1"
driver.get(url)

# Allow time for the page to load
time.sleep(30)

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Function to clean up Unicode characters
def clean_text(text):
    # Replace Unicode non-breaking spaces with regular spaces
    text = text.replace('\u00a0', ' ')
    return text

# Create a list to store product data
products = []

# Extract product details
for product in soup.find_all('div', class_='style_card_details__qi0G9'):
    try:
        # Extract product name
        name = clean_text(product.find('h3', class_='style_prod_name__QllSp').text.strip())

        # Extract the price section
        price_section = product.find('h6', class_='style_prod_price__4TltC')

        # Extract MRP
        mrp_span = price_section.find('span', class_='style_striked_price__4ghn5')
        standard_price = clean_text(mrp_span.text.strip()) if mrp_span else "N/A"

        # Extract selling price
        selling_price_span = price_section.find('span', class_='style_selling_price__GaIsF')
        selling_price = clean_text(selling_price_span.text.strip()) if selling_price_span else "N/A"

        # Extract final price
        final_price_section = product.find('p', class_='style_final_price__FERLK')
        final_price = clean_text(final_price_section.text.strip()) if final_price_section else "N/A"

        # Extract product quantity
        quantity = clean_text(product.find('span', class_='style_prod_qt__cXcqe').text.strip())

        # Add product to the list as a dictionary
        products.append({
            'Name': name,
            'Standard Price (MRP)': standard_price,
            'Selling Price': selling_price,
            'Final Price': final_price,
            'Quantity': quantity
        })
    except Exception as e:
        print(f"Error extracting product details: {e}")

# Save the scraped data to a JSON file
with open('products.json', 'w', encoding='utf-8') as json_file:
    json.dump(products, json_file, indent=4, ensure_ascii=False)

print(f"Scraped {len(products)} products and saved to products.json")
