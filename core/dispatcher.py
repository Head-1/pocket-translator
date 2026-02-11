from config import settings

from providers.local.translator import LocalTranslator
from providers.local.transliterator import LocalTransliterator

from providers.azure.translator import AzureTranslator
from providers.azure.transliterator import AzureTransliterator


class Dispatcher:

    def __init__(self, provider: str | None = None):
        self.provider = provider or settings.provider
        self._load_providers()

    def _load_providers(self):

        if self.provider == "azure" and settings.azure_key and settings.azure_endpoint:
            self.translator = AzureTranslator()
            self.transliterator = AzureTransliterator()

        else:
            # Fallback automático
            self.provider = "local"
            self.translator = LocalTranslator()
            self.transliterator = LocalTransliterator()

    def translate(self, text, source, target):
        return self.translator.translate(text, source, target)

    def transliterate(self, text, language, script):
        return self.transliterator.transliterate(text, language, script)
