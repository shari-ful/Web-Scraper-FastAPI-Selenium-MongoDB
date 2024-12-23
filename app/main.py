from fastapi import FastAPI


app = FastAPI(title='Scrape Website With FastAPI, Celery, Selenium and MongoDB')

@app.get('/')
async def index():
    return "App is running"