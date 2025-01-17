from .logger import logger
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.responses import HTMLResponse



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Cargar el formulario de búsqueda
@app.get("/busqueda", response_class=HTMLResponse)
async def read_root(request: Request):
    logger.info("Cargando el formulario de busqueda")
    return templates.TemplateResponse("search.html", {"request": request})


# route for the search form
@app.get("/carga", response_class=HTMLResponse)
async def read_root(request: Request):
    logger.info("Cargando el formulario de carga de monumentos")
    return templates.TemplateResponse("load.html", {"request": request})

