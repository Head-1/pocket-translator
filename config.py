import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    def __init__(self):
        self.provider = os.getenv("PROVIDER", "local")

        # Azure
        self.azure_endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
        self.azure_key = os.getenv("AZURE_TRANSLATOR_KEY")
        self.azure_region = os.getenv("AZURE_TRANSLATOR_REGION")


settings = Settings()
