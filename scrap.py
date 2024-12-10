import requests
from bs4 import BeautifulSoup

def scrape_real_estate(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find specific elements based on HTML tags and attributes
    property_title = soup.find('h1', {'class': 'property-title'}).text.strip()
    price = soup.find('span', {'class': 'price'}).text.strip()
    # ... other elements

    # Store data in a dictionary
    property_data = {
        'title': property_title,
        'price': price,
        # ... other fields
    }

    return property_data

# Example usage:
url = 'https://www.example-real-estate.com/property-listing'
property_info = scrape_real_estate(url)

# Save data to a JSON file
import json

with open('real_estate_data.json', 'w') as f:
    json.dump(property_info, f)