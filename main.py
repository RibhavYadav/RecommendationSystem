from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from backend.recommender import hexValueGenerator

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("frontend/index.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/random-colour")
async def get_random_colour():
    colour = hexValueGenerator()
    return {"colour": colour}
