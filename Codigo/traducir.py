# traducir.py

from langdetect import detect
from deep_translator import GoogleTranslator

def detectar_idioma(texto: str) -> str:
    """
    Detecta el idioma del texto usando langdetect.
    Devuelve un código ISO como 'es', 'en', 'fr', etc.
    """
    try:
        return detect(texto)
    except Exception:
        return "es"  # fallback si error en detección


def traducir(texto: str, origen="auto", destino="es") -> str:
    """
    Traduce un texto desde 'origen' a 'destino' usando GoogleTranslator.
    Si falla, devuelve el texto original.
    """
    try:
        return GoogleTranslator(source=origen, target=destino).translate(texto)
    except Exception:
        return texto