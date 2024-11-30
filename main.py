from fastapi import FastAPI
import requests

app = FastAPI()

NEWS_API_KEY = "1d73d7cd8ecb4dfe9a21def3f511c2da"  
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(country="us", category="general"):
    params = {
        "country": country,
        "category": category,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code == 200:
        return response.json()  # Return the news data in JSON format
    else:
        return {"error": "Unable to fetch news"}

@app.get("/news/{country}/{category}")
async def get_news(country: str, category: str):
    news = fetch_news(country, category)
    return news

