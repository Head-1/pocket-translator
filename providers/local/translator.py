from deep_translator import GoogleTranslator
from core.interfaces import TranslatorProvider


class LocalTranslator(TranslatorProvider):

    def translate(self, text: str, source: str, target: str) -> str:
        return GoogleTranslator(source=source, target=target).translate(text)
