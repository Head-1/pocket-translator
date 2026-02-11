from abc import ABC, abstractmethod


class TranslatorProvider(ABC):

    @abstractmethod
    def translate(self, text: str, source: str, target: str) -> str:
        pass


class TransliteratorProvider(ABC):

    @abstractmethod
    def transliterate(self, text: str, language: str, script: str) -> str:
        pass
