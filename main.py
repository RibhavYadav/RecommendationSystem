from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from backend.recommender import Recommender
import uvicorn

app = FastAPI()
recommender = Recommender()
app.mount("/static", StaticFiles(directory="frontend"), name="static")


class ColorData(BaseModel):
    colour: str


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
    rgb_value = data.colour[4:-2].split(",")
    lst = []
    for val in rgb_value:
        val = val.strip()
        if not val:
            lst.append(0)
        else:
            lst.append(int(val),)
    recommender.chosen_colours.append(lst)

    return {"received_color": data.colour}


if __name__ == "__main__":
    uvicorn.run("main:app")
