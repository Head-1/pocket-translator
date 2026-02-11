import os
import requests
from core.interfaces import TransliteratorProvider


class AzureTransliterator(TransliteratorProvider):

    def transliterate(self, text: str, language: str, script: str):

        endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
        key = os.getenv("AZURE_TRANSLATOR_KEY")

        if not endpoint or not key:
            raise EnvironmentError("Azure Translator not configured")

        # Endpoint real: /transliterate

        raise NotImplementedError("Azure Transliterator stub")
