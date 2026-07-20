from .collectors.world_bank import WorldBankCollector
from .collectors.imf import IMFCollector
from .collectors.faostat import FAOSTATCollector
from .collectors.comtrade import ComtradeCollector
import pandas as pd

def run_etl():
    print("Démarrage du pipeline ETL CEIP...")
    all_dfs = []
    
    # Banque mondiale
    wb = WorldBankCollector()
    df_wb = wb.collect_all()
    all_dfs.append(df_wb)
    print(f"World Bank : {len(df_wb)} lignes")
    
    # IMF
    imf = IMFCollector()
    df_imf = imf.collect_all()
    all_dfs.append(df_imf)
    print(f"IMF : {len(df_imf)} lignes")
    
    # FAO
    fao = FAOSTATCollector()
    df_fao = fao.collect_all()
    all_dfs.append(df_fao)
    print(f"FAO : {len(df_fao)} lignes")
    
    # Comtrade
    com = ComtradeCollector()
    df_com = com.collect_all()
    all_dfs.append(df_com)
    print(f"Comtrade : {len(df_com)} lignes")
    
    # Fusionner tous les DataFrames (pour l'instant on les retourne)
    if all_dfs:
        merged = pd.concat(all_dfs, ignore_index=True)
        print(f"Total : {len(merged)} lignes collectées")
        # Ici on pourrait insérer dans la base de données (plus tard)
        return merged
    else:
        return pd.DataFrame()