from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from backend.recommender import Recommender, ColorData
import uvicorn

app = FastAPI()
recommender = Recommender()
app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("frontend/index.html") as f:
        return HTMLResponse(content=f.read())


@app.get("/random-colour")
async def send_random_colour():
    colour = recommender.get_colour()
    return {"colour": colour}


@app.post("/get-colour")
async def get_button_colour(data: ColorData):
    colour = recommender.parse_colour_data(data)
    recommender.chosen_colours.append(colour)
    return {"received_color": data.colour}


@app.post("/save-colour")
async def save_colour(data: ColorData):
    colour = recommender.parse_colour_data(data)
    recommender.saved_colours.append(colour)
    return {"received_color": data.colour}


if __name__ == "__main__":
    uvicorn.run("main:app")
