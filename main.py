from data.database import database
from typing import Annotated
from data.modelo.menu import Menu

from data.dao.dao_usuarios import DaoUsuarios

from typing import Union

from fastapi import FastAPI, Request, Form


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/")
def read_root():
    return RedirectResponse(url="/home")


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    
   
    return templates.TemplateResponse(
        request=request, name="base-index.html", #context={"nombre": "pepe"}                                                      
    )

@app.get("/registrarse", response_class=HTMLResponse)
async def registrarse(request: Request):
    
   
    return templates.TemplateResponse(
        request=request, name="base-registrarse.html" #context={"nombre": "pepe"}                                                      
    )

@app.get("/recursos", response_class=HTMLResponse)
async def recursos(request: Request):
    
   
    return templates.TemplateResponse(
        request=request, name="base-recursos.html", #context={"nombre": "pepe"}                                                      
    )
    
    
@app.get("/utilesrise", response_class=HTMLResponse)
async def utilesrise(request: Request):
    
   
    return templates.TemplateResponse(
        request=request, name="base-utilesMHRise.html", #context={"nombre": "pepe"}                                                      
    )

@app.get("/usuarios")
def get_usuarios(request: Request):

    usuarios =  DaoUsuarios().get_all(database)
    

    return templates.TemplateResponse(
    request=request, name="base-usuarios.html", context={"usuarios": usuarios})

@app.get("/deleteusuarios/{usuario_id}")
def delete_usuarios(request: Request,usuario_id:str):
    dao = DaoUsuarios()
    dao.delete(database, usuario_id)
    
    usuarios =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="base-usuarios.html", context={"usuarios": usuarios}                                                      
)

  

@app.post("/delusuarios")
def del_usuarios(request: Request,usuario_id:Annotated[str, Form()] ):
    print("brawl")
    dao = DaoUsuarios()
    dao.delete(database, usuario_id)
    
    usuarios =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="base-usuarios.html", context={"usuarios": usuarios} )
    
@app.get("/formaddusuarios")
def form_add_usuarios(request: Request):
    return templates.TemplateResponse(
    request=request, name="formaddusuarios.html"
    )

@app.post("/addusuarios")
def add_usuarios(request: Request,id: Annotated[int, Form()], nombre: Annotated[str, Form()] = None):
    if nombre is None or id is None:
        return templates.TemplateResponse(
        request=request, name="base-usuarios.html", context={"nombre": "pepe"}
        )
    
    dao = DaoUsuarios()
    dao.insert(database,id, nombre)
    
    usuarios =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="formaddusuarios.html", context={"usuarios": usuarios}                                                      
)    