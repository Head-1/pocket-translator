from core.interfaces import TransliteratorProvider


class LocalTransliterator(TransliteratorProvider):

    def transliterate(self, text: str, language: str, script: str) -> str:
        # Fallback simples: retorna texto original
        # Pode ser substituído por lib futura
        return text
