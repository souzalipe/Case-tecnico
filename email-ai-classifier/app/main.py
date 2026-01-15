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

def classify_email_rule_based(email_text: str) -> str:
    productive_keywords = [
        "reunião", 
        "projeto", 
        "prazo", 
        "relatório"
        "entrega",
        "cliente",
        "alinhamento",
        "follow-up"
        ]
    
    text_lower = email_text.lower()
    
    for keyword in productive_keywords:
        if keyword in text_lower:
            return "Produtivo"
    
    return "Não Produtivo"

@app.post("/process", response_class=HTMLResponse)
def process_email(request: Request, email_text: str = Form(...)):

    category = classify_email_rule_based(email_text)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "email_text": email_text,
            "category": category
        }
    )
