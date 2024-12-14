from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from backend.recommender import random_rgb_generator
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")


class ColorData(BaseModel):
    colour: str


@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("frontend/index.html") as f:
        return HTMLResponse(content=f.read())


@app.get("/random-colour")
async def send_random_colour():
    colour = random_rgb_generator()
    return {"colour": colour}


@app.post("/get-colour")
async def get_colour(data: ColorData):
    return {"received_color": data.colour}


if __name__ == "__main__":
    uvicorn.run("main:app")
