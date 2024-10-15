import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Path to Chrome driver
chrome_driver_path = 'C:\chromedriver\chromedriver.exe'

options = webdriver.ChromeOptions()
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.amazon.in/POOCH-FURR-Vitamins-Glucosamine-Advantage/dp/B0CXJBQPRS/ref=sr_1_2_sspa?crid=296CGNGAMMK1M&dib=eyJ2IjoiMSJ9._7GM9N6Uc27paTzRNTKxhxIMWjXE4xzRD38mmPqId7MfFRYgSaILtEIX1xMES_4_Evua83Iue4ENzSt0m0X6yHtBTme6zztqMZCS2AWBzmKYk283mKvG_l418a2neR7Eye_-Pk5o93GvUmfRHIWzIkfdn4mqLnaqfERlfs7XhsDNjMsZEqCd7qa95TKKdvTJFHlB00-gJStudgaLPNwlutupDb_MJaFR6HcgoG6DCr0ur5qxb6iJU5iWnWfi_qYNWUHSuIvus2VS1gYGmCzPZU8QolUw6RF_qGYY8EeidS4.uJrgXKipLAoyADrf_6mfvnq8I6VT1iaI6BEOwo_cAEA&dib_tag=se&keywords=salmon%2Boil%2Bfor%2Bdogs&qid=1728969348&rnid=2454181031&s=pet-supplies&sprefix=sal%2Cpets%2C250&sr=1-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

product_data = []

for product_detail in soup.find_all('div', id="centerCol"):

    product_name = product_detail.find(id="productTitle").text.strip() if soup.find(id="productTitle") else "N/A"

    average_rating = product_detail.find('span', class_="a-icon-alt").text.strip() if soup.find(class_="a-icon-alt") else "N/A"

    total_rating = product_detail.find('span', id="acrCustomerReviewText").text.strip() if soup.find(id="acrCustomerReviewText") else "N/A"

    mrp = product_detail.find(class_="a-size-small aok-offscreen").text.strip().split("M.R.P.:")[1] if soup.find(class_="a-size-small aok-offscreen") else "N/A"


    selling_price = product_detail.find('span', class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").text.strip() if soup.find(class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay") else "N/A"

    discount = product_detail.find('span', class_="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage").text.strip() if soup.find(class_="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage") else "N/A"

    specs = soup.find(class_ = 'a-normal a-spacing-micro')
    specs_keys = specs.find_all(class_ = 'a-size-base a-text-bold')
    specs_value = specs.find_all(class_ = 'a-size-base po-break-word')

    specs_dict = {}
    for i in range(len(specs_keys)):
        specs_dict[specs_keys[i].text] = specs_value[i].text
    print(specs_dict)

    discription = soup.find(id="featurebullets_feature_div")
    discription_data = discription.find_all(class_="a-list-item").text.strip()


    



    

product_data.append({
    # 'Name' : product_name,
    # 'Average Rating' : average_rating,
    # 'Total Rating' : total_rating,
    # 'MRP' : mrp,
    # 'Selling Price' : selling_price,
    # 'Discount' : discount,
    #'Specification' : specs_dict
    'About This Item' : discription_data
    
})

#with open("products.json", "w") as json_file:
 #   json.dump(product_data, json_file, indent=4)

print(product_data)
# print(table_content)