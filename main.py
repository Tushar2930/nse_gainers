import requests
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime


def fetch_data():
    url = "https://www.nseindia.com/api/live-analysis-variations?index=gainers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.nseindia.com/market-data/top-gainers-losers"
    }

    session = requests.Session()
    response = session.get(url, headers=headers)
    # Parse the F&O securities data
    fo_securities_data = response.json()

    # Store data
    filename = f"fo_securities_{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(filename, 'w') as file:
        json.dump(fo_securities_data, file, indent=4)

    print(f"Data for {datetime.now().strftime('%Y-%m-%d')} saved to {filename}")


if __name__ == "__main__":
    fetch_data()