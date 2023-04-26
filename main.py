import uvicorn
from fastapi import FastAPI

from app.routers import web_scraping

app = FastAPI()

app.include_router(web_scraping.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
