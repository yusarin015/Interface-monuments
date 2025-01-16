from .logger import logger
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Cargar el formulario de búsqueda
@app.get("/busqueda", response_class=HTMLResponse)
async def read_root(request: Request):
    logger.info("Cargando el formulario de busqueda")
    return templates.TemplateResponse("search.html", {"request": request})

