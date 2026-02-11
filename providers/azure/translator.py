import os
import requests
from core.interfaces import TranslatorProvider


class AzureTranslator(TranslatorProvider):

    def translate(self, text: str, source: str, target: str) -> str:

        endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
        key = os.getenv("AZURE_TRANSLATOR_KEY")
        region = os.getenv("AZURE_TRANSLATOR_REGION")

        if not endpoint or not key:
            raise EnvironmentError("Azure Translator not configured")

        url = f"{endpoint}/translate"
        params = {
            "api-version": "3.0",
            "from": source,
            "to": target,
        }

        headers = {
            "Ocp-Apim-Subscription-Key": key,
            "Ocp-Apim-Subscription-Region": region,
            "Content-Type": "application/json",
        }

        body = [{"text": text}]

        # DESCOMENTE quando tiver Azure:
        # response = requests.post(url, params=params, headers=headers, json=body)
        # response.raise_for_status()
        # return response.json()[0]["translations"][0]["text"]

        raise NotImplementedError("Azure Translator stub")
