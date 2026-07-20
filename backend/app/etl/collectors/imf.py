import requests
import pandas as pd

class IMFCollector:
    BASE_URL = "https://www.imf.org/external/datamapper/api/v1"
    COUNTRIES = {"CMR": "CMR", "GAB": "GAB", "COG": "COG", "TCD": "TCD", "CAF": "CAF", "GNQ": "GNQ"}
    INDICATORS = {
        "GDP_GROWTH": "NGDP_RPCH",
        "INFLATION": "PCPIPCH",
        "DEBT_GDP": "GGXWDG_NGDP",
        "CURRENT_ACCOUNT": "BCA_NGDPD",
    }
    
    def collect_all(self):
        all_data = []
        current_year = pd.Timestamp.now().year
        years = list(range(2000, current_year+1))
        
        for name, code in self.INDICATORS.items():
            url = f"{self.BASE_URL}/{code}"
            params = {"periods": ",".join(str(y) for y in years)}
            resp = requests.get(url, params=params)
            if resp.status_code == 200:
                data = resp.json()
                values = data.get("values", {}).get(code, {})
                for country_code, country_data in values.items():
                    if country_code not in self.COUNTRIES.values():
                        continue
                    for period, value in country_data.items():
                        if value is not None:
                            all_data.append({
                                "country": country_code,
                                "indicator": name,
                                "date": period,
                                "value": float(value)
                            })
        df = pd.DataFrame(all_data)
        if not df.empty:
            df["source"] = "IMF DataMapper"
        return df