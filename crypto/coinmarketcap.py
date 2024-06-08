import requests
from bs4 import BeautifulSoup

class CoinMarketCap:
    def __init__(self, coin):
        self.coin = coin
        self.base_url = "https://coinmarketcap.com/coins/"

    def fetch_data(self):
        url = f"{self.base_url}{self.coin}/"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch data for {self.coin}")

    def parse_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        data = {}
        
        # Example scraping logic (you will need to adapt this to the actual HTML structure)
        price_tag = soup.find('div', class_='priceValue')
        data['price'] = float(price_tag.text.replace('$', '').replace(',', '')) if price_tag else None
        
        # Additional data parsing logic...
        return data

    def get_coin_data(self):
        html = self.fetch_data()
        return self.parse_data(html)
