import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get("/rating")
def get_rating():
    url = "https://www.surf-forecast.com/breaks/Zurriola-hondartza/forecasts/latest"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # 1️⃣ Intento 1: rating directo como texto (★★★☆☆)
    rating_text = soup.find(class_="rating")
    if rating_text:
        stars = rating_text.text.strip()
        return {"rating": stars}

    # 2️⃣ Intento 2: rating como spans con clases .on / .half
    star_container = soup.find(class_="rating-stars")
    if star_container:
        stars_on = len(star_container.find_all("span", class_="on"))
        stars_half = len(star_container.find_all("span", class_="half"))
        rating = stars_on + 0.5 * stars_half
        return {"rating": rating}

    return {"error": "No se pudo encontrar el rating"}