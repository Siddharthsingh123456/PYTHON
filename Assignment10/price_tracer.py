
"""
Price Tracer Application
Created as part of Web Scraping Assignment.

My Learning Process:
1. Learned how to send requests to a website.
2. Learned how to inspect HTML elements.
3. Used BeautifulSoup to extract data.
4. Converted price text into a numeric value.
5. Compared the current price with a target price.
"""

import requests
from bs4 import BeautifulSoup
import re
import os

product_urls = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
]

target_price = 20.0
os.makedirs("images", exist_ok=True)

for url in product_urls:
    print("\n" + "="*50)
    print("Practical Output: Processing URL")
    print(url)

    try:
        # Step 1
        print("Step 1: Sending request to website")
        response = requests.get(url, timeout=10)

        # Step 2
        print("Step 2: Parsing HTML content")
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 3
        print("Step 3: Extracting product title")
        title = soup.find("h1").text.strip()

        # Step 4
        print("Step 4: Extracting product price")
        price_text = soup.find("p", class_="price_color").text.strip()

        # Converting string price to numeric value
        price = float(re.sub(r"[^0-9.]", "", price_text))

        # Step 5
        print("Step 5: Extracting image URL")
        image_tag = soup.find("img")
        image_url = "https://books.toscrape.com/" + image_tag["src"].replace("../", "")

        print("Title :", title)
        print("Price :", price)
        print("Image URL :", image_url)

        # Step 6
        print("Step 6: Downloading image")
        image_data = requests.get(image_url).content
        filename = title.replace(" ", "_") + ".jpg"

        with open(os.path.join("images", filename), "wb") as file:
            file.write(image_data)

        print("Image saved as:", filename)

        # Step 7
        print("Step 7: Comparing price with target price")

        if price <= target_price:
            print("Result: Price is BELOW target price")
        else:
            print("Result: Price is ABOVE target price")

    except Exception as e:
        print("Error occurred:", e)
