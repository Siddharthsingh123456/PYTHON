import time, csv
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
print("Driver Initiated")

driver.get('http://quotes.toscrape.com')

# Data container
quotes_data = []


while True:
    # Wait for the page to load (optional delay)
    time.sleep(1)

    # Extract all quote blocks
    quotes = driver.find_elements(By.CLASS_NAME, 'quote')

    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, 'text').text.strip()
        author = quote.find_element(By.CLASS_NAME, 'author').text.strip()
        tags_elements = quote.find_elements(By.CLASS_NAME, 'tag')
        tags = [tag.text for tag in tags_elements]

        quotes_data.append({
            'quote': text,
            'author': author,
            'tags': ', '.join(tags)
        })

    # Check if there's a next page
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'li.next > a')
        next_button.click()
    except:
        break  # No more pages

# Close browser
driver.quit()

with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['quote', 'author', 'tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for quote in quotes_data:
        writer.writerow(quote)

print("✅ Data extraction complete. Saved to 'quotes.csv'")