# 📄 README.md (English)

# Pocket Translator — Azure-Ready Linguistic Assistant

🇧🇷 Leia em Português → [README.pt-BR.md](README.pt-BR.md)

Pocket Translator is a CLI-first linguistic assistant designed for students and professionals who need **technical translation and transliteration** workflows.

The project is built with a **provider-based architecture**, prioritizing **Azure AI Translator** while supporting local and alternative engines for offline development and testing.

It is fully compatible with Linux, macOS, Windows, and Android devices via **Termux**, enabling mobile edge usage.

---

## 🎯 Goals

- Provide technical text translation via CLI
- Support transliteration pipelines
- Be Azure AI Translator ready
- Enable multi-provider engines
- Run on mobile environments (Termux)
- Serve as a foundation for future Edge orchestration systems

---

## 🧠 Architecture Overview

The system follows a modular, provider-driven design:

```

pocket-translator/
├── main.py
├── config.py
├── core/
│   ├── interfaces.py
│   └── dispatcher.py
├── providers/
│   ├── azure/
│   │   ├── translator.py
│   │   └── transliterator.py
│   └── local/
│       ├── translator.py
│       └── transliterator.py
├── cli/
│   └── app.py
└── docs/
└── architecture.md

````

### Key Concepts

- **Dispatcher Pattern** — dynamically selects providers
- **Interface Contracts** — enforce translation and transliteration APIs
- **Azure-first Design** — ready for Cognitive Services integration
- **Fallback Providers** — allow offline development
- **CLI-first UX** — minimal, automation-friendly interface

---

## ☁️ Azure Integration

Azure providers are implemented using REST APIs and environment variables:

```bash
AZURE_TRANSLATOR_ENDPOINT=
AZURE_TRANSLATOR_KEY=
AZURE_TRANSLATOR_REGION=
````

When configured, simply run:

```bash
python main.py translate "Hello world" --provider azure
```

---

## 📱 Mobile / Termux Support

Pocket Translator runs natively in Termux:

```bash
pkg install python
pip install -r requirements.txt
python main.py translate "Edge computing is powerful"
```

---

## ▶️ Usage

### Translate

```bash
python main.py translate "Cloud systems scale fast" --source en --target pt
```

### Transliterate

```bash
python main.py transliterate "こんにちは" ja Latn
```

### Provider via Environment

```bash
export PROVIDER=local
python main.py translate "Cloud native platforms"
```

---

## 🛣️ Roadmap

**v1.0 — Bootcamp MVP**

* CLI translator
* Transliteration pipeline
* Azure-ready providers
* Multi-engine support
* Termux compatibility

**v2.0 — Edge Expansion**

* Skuld MCP orchestration integration
* Mobile daemon mode
* REST API
* Containerized agents
* Control-plane driven execution

---

## 🧩 Inspiration

This architecture is inspired by edge orchestration systems designed for mobile environments, demonstrating how cloud AI services can be embedded into portable devices.

---

## 📜 License

Educational / Open Source use.

---

## 👤 Author

Built for Microsoft Azure AI Bootcamp Challenge.

**AMJR**
