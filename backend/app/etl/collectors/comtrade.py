import requests
import pandas as pd

class ComtradeCollector:
    BASE_URL = "https://comtradeapi.un.org/public/v1"
    COUNTRIES = {"CMR": 120, "GAB": 266, "COG": 178, "TCD": 148, "CAF": 140, "GNQ": 226}
    
    def collect_all(self, year=2023):
        all_data = []
        for country_code, reporter in self.COUNTRIES.items():
            for flow, code in [("EXPORT", "X"), ("IMPORT", "M")]:
                url = f"{self.BASE_URL}/preview/C/A/HS"
                resp = requests.get(url, params={"reporterCode": reporter, "period": year, "flowCode": code})
                if resp.status_code == 200:
                    data = resp.json()
                    for row in data.get("data", []):
                        all_data.append({
                            "country": country_code,
                            "indicator": flow,
                            "date": str(year),
                            "value": row.get("TradeValue")
                        })
        df = pd.DataFrame(all_data)
        df["source"] = "UN Comtrade"
        return df