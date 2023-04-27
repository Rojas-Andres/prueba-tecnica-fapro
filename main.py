from fastapi import FastAPI

from app.routers import web_scraping

app = FastAPI(title="API Fapro", version="0.1.0")

app.include_router(web_scraping.router)
