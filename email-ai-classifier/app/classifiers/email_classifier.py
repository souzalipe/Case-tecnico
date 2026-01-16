from app.classifiers.ai_classifier import classify as ai_classify
from app.classifiers.rule_classifier import classify as rule_classify
import logging

logger = logging.getLogger(__name__)

def classify_email(text: str) -> dict:
    ai_result = ai_classify(text)

    if ai_result["method"] == "ai":
        return ai_result

    logger.warning("IA indisponível. Usando classificador por regras.")
    return rule_classify(text)
