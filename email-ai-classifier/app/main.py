from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/process", response_class=HTMLResponse)
def process_email(request: Request, email_text: str = Form(...)):
    # CLASSIFICAÇÃO TEMPORÁRIA (fake)
    category = "Produtivo"

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "email_text": email_text,
            "category": category
        }
    )
