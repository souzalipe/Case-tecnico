import logging

logger = logging.getLogger(__name__)

# Regras simples por palavras-chave
RULES = {
    "financeiro": ["fatura", "boleto", "pagamento", "nota fiscal", "cobrança"],
    "suporte": ["erro", "problema", "falha", "não funciona", "bug"],
    "comercial": ["preço", "orçamento", "proposta", "contrato"],
    "spam": ["ganhe dinheiro", "promoção", "clique aqui", "oferta imperdível"]
}

def classify(text: str) -> dict:
    text_lower = text.lower()

    for category, keywords in RULES.items():
        for keyword in keywords:
            if keyword in text_lower:
                logger.info(f"Classificado por regra: {category}")
                return {
                    "category": category,
                    "confidence": 0.80,
                    "method": "rules"
                }

    logger.info("Nenhuma regra aplicada. Classificado como 'outros'")
    return {
        "category": "outros",
        "confidence": 0.50,
        "method": "rules"
    }
