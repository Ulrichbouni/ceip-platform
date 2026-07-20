import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api.v1 import etl

load_dotenv()

app = FastAPI(title="CEIP API", version="1.0")

# Autoriser les requêtes depuis votre futur site (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(etl.router, prefix="/api/v1/etl", tags=["etl"])

# Route de test
@app.get("/")
def root():
    return {"message": "CEIP API is running"}

# Route qui renverra les données économiques (après ETL)
@app.get("/api/v1/dashboard/macro")
def get_macro_data():
    # Pour l'instant, renvoie un exemple ; plus tard, on interrogera la base
    return {
        "countries": ["CMR", "GAB", "COG", "TCD", "CAF", "GNQ"],
        "indicators": ["GDP_GROWTH", "CPI", "DEBT"],
        "message": "Les données réelles arrivent après le pipeline ETL"
    }

# On ajoutera les routes ETL plus tard