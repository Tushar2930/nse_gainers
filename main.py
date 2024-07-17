import requests
from bs4 import BeautifulSoup
import schedule
import time
import json
from datetime import datetime
def fetch_data():
    url = "https://www.nseindia.com/market-data/top-gainers-losers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    session = requests.Session()
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Parse the F&O securities data
    fo_securities_data = []

    # Example parsing - Adjust according to the actual HTML structure
    for row in soup.find_all('div', class_='table-responsive'):
        security = {}
        security['name'] = row.find('td', class_='security_name').text
        security['price'] = row.find('td', class_='last_price').text
        security['change'] = row.find('td', class_='change').text
        security['percent_change'] = row.find('td', class_='percent_change').text
        fo_securities_data.append(security)

    # Store data
    filename = f"fo_securities_{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(filename, 'w') as file:
        json.dump(fo_securities_data, file, indent=4)

    print(f"Data for {datetime.now().strftime('%Y-%m-%d')} saved to {filename}")

# Schedule the task to run daily at 9:30 AM IST
schedule.every().day.at("15:50").do(fetch_data)

while True:
    schedule.run_pending()
    time.sleep(60)
