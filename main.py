from .logger import logger
from .api.routes.extractor import router as ExtractorRouter
from api.routes.search import router as SearchRouter
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# route for the search form
@app.get("/carga", response_class=HTMLResponse)
async def read_root(request: Request):
    logger.info("Cargando el formulario de carga de monumentos")
    return templates.TemplateResponse("load.html", {"request": request})