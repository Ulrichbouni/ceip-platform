import requests
import pandas as pd

class WorldBankCollector:
    BASE_URL = "http://api.worldbank.org/v2"
    INDICATORS = {
        "GDP_GROWTH": "NY.GDP.MKTP.KD.ZG",
        "CPI": "FP.CPI.TOTL.ZG",
        "DEBT": "GC.DOD.TOTL.GD.ZS",
        "POPULATION": "SP.POP.TOTL",
    }
    COUNTRIES = ["CMR", "GAB", "COG", "TCD", "CAF", "GNQ"]
    
    def collect_all(self):
        all_data = []
        for country in self.COUNTRIES:
            for name, code in self.INDICATORS.items():
                url = f"{self.BASE_URL}/country/{country}/indicator/{code}"
                resp = requests.get(url, params={"format": "json", "per_page": 1000})
                if resp.status_code == 200:
                    data = resp.json()
                    if len(data) > 1:
                        for item in data[1]:
                            if item.get("value"):
                                all_data.append({
                                    "country": country,
                                    "indicator": name,
                                    "date": item["date"],
                                    "value": float(item["value"])
                                })
        df = pd.DataFrame(all_data)
        df["source"] = "World Bank"
        return df