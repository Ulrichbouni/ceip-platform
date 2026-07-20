import requests
import pandas as pd

class FAOSTATCollector:
    BASE_URL = "https://fenixservices.fao.org/faostat/api/v1/en"
    COUNTRIES = {"CMR": 27, "GAB": 79, "COG": 48, "TCD": 148, "CAF": 36, "GNQ": 67}
    
    def collect_all(self):
        all_data = []
        for country_code, area_code in self.COUNTRIES.items():
            url = f"{self.BASE_URL}/data/QCL"
            params = {"area_code": area_code, "item_code": "56"}  # Maïs
            resp = requests.get(url, params=params)
            if resp.status_code == 200:
                data = resp.json()
                for item in data.get("data", []):
                    all_data.append({
                        "country": country_code,
                        "indicator": "MAIZE_PRODUCTION",
                        "date": item.get("Year"),
                        "value": item.get("Value")
                    })
        df = pd.DataFrame(all_data)
        df["source"] = "FAO"
        return df