from config import PROVIDER
from providers.local.translator import LocalTranslator
from providers.local.transliterator import LocalTransliterator
from providers.azure.translator import AzureTranslator
from providers.azure.transliterator import AzureTransliterator


class Dispatcher:

    def __init__(self, provider=None):

        self.provider = provider or PROVIDER

        if self.provider == "local":
            self.translator = LocalTranslator()
            self.transliterator = LocalTransliterator()

        elif self.provider == "azure":
            self.translator = AzureTranslator()
            self.transliterator = AzureTransliterator()

        else:
            raise ValueError(f"Provider not supported: {self.provider}")

    def translate(self, text, source, target):
        return self.translator.translate(text, source, target)

    def transliterate(self, text, language, script):
        return self.transliterator.transliterate(text, language, script)
