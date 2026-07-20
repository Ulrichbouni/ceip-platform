from fastapi import APIRouter, BackgroundTasks
from app.etl.pipeline import run_etl

router = APIRouter()

@router.post("/run")
def start_etl(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_etl)
    return {"status": "ETL started", "message": "Les données sont en cours de collecte"}