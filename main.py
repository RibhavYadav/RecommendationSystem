from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("frontend/static/index.html") as f:
        return HTMLResponse(content=f.read())
