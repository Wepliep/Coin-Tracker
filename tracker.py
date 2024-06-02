import requests
import pandas as pd
import json
import sys
import argparse
from datetime import datetime
import matplotlib.pyplot as plt

try:
    with open("url.config", "r") as f:
        api_urls = json.load(f)
except FileNotFoundError:
    print("HATA: Konfigürasyon dosyası olan 'url.config' bulunamadı.")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"HATA:  JSON kod çözme hatası 'url.config': {e}")
    sys.exit(1)

parser = argparse.ArgumentParser(
    description="Kripto para fiyatlarını alın ve grafiği çizin.",
    formatter_class=argparse.RawTextHelpFormatter
)



token = args.token.upper()
if token not in api_urls:
    print(f"Error: Token '{token}' not found in the configuration file.")
    sys.exit(1)

api_url = api_urls[token]

params = {
    "vs_currency": "try",  # Türk Lirası
    "days": "30"  # Son 30 gün
}


response = requests.get(api_url, params=params)
data = response.json()
prices = data["prices"]
df = pd.DataFrame(prices, columns=["timestamp", "price"])
df["date"] = pd.to_datetime(df["timestamp"], unit='ms')
df.drop("timestamp", axis=1, inplace=True)
print(df)