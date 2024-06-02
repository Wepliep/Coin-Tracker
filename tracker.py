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

