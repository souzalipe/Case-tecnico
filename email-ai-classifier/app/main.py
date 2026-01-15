USE_AI_CLASSIFIER = False  # Defina como True para usar o classificador AI, False para usar a classificação baseada em regras

import logging
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
    )


app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

def classify_email_rule_based(email_text: str) -> str: # Classificação simples baseada em palavras-chave
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
    
    text_lower = email_text.lower() # Converte o texto para minúsculas para facilitar a comparação
    
    for keyword in productive_keywords:
        if keyword in text_lower:
            return "Produtivo"
    
    return "Não Produtivo"

def classify_email(text: str) -> str:
    strategy = "AI" if USE_AI_CLASSIFIER else "RULE_BASED"
    result = (
        classify_email_ai(text)
        if USE_AI_CLASSIFIER
        else classify_email_rule_based(text)
    )

    logging.info(
        "Classification executed | strategy=%s | result=%s | text_preview=%s",
        strategy,
        result,
        text[:80].replace("\n", " ")
    )

    return result


def classify_email_ai(text: str) -> str: # Classificação usando modelo AI
    
    return "Produtivo" # Placeholder para integração futura com modelo AI

@app.post("/process", response_class=HTMLResponse)
def process_email(request: Request, email_text: str = Form(...)): # O "Form(...)" é importante porque diz -> “esse valor vem de um formulário HTML (POST)” e precisa ser importado

    category = classify_email(email_text)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "email_text": email_text,
            "category": category
        }
    )
