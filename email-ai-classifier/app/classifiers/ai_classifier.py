# Prompt -> Classifique o email abaixo como "Produtivo" ou "Não Produtivo" e sugira uma resposta curta e profissional.

import logging

logger = logging.getLogger(__name__)

_classifier = None

def get_classifier():
    global _classifier

    if _classifier is None:
        try:
            from transformers import pipeline
            _classifier = pipeline(
                "text-classification",
                model="distilbert-base-uncased-finetuned-sst-2-english"
            )
            logger.info("Classificador de IA carregado com sucesso")
        except Exception as e:
            logger.error(f"Falha ao carregar IA: {e}")
            _classifier = None

    return _classifier


def classify(text: str) -> dict:
    classifier = get_classifier()

    if classifier is None:
        return {
            "category": "indefinido",
            "confidence": 0.0,
            "method": "ai_unavailable"
        }

    result = classifier(text)[0]

    return {
        "category": result["label"],
        "confidence": float(result["score"]),
        "method": "ai"
    }
