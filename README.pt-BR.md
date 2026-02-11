# 📄 README.pt-BR.md (Português)

```markdown
# Pocket Translator — Assistente Linguístico Azure-Ready

🇺🇸 Read in English → [README.md](README.md)

Pocket Translator é um assistente linguístico em linha de comando (CLI) voltado para estudantes e profissionais que precisam de **tradução técnica e transliteração**.

O projeto foi construído com uma **arquitetura baseada em provedores**, priorizando o **Azure AI Translator**, ao mesmo tempo que permite motores locais para desenvolvimento e testes offline.

É compatível com Linux, macOS, Windows e Android via **Termux**, permitindo uso em ambientes mobile.

---

## 🎯 Objetivos

- Tradução de textos técnicos via CLI
- Pipeline de transliteração
- Integração com Azure AI Translator
- Suporte a múltiplos provedores
- Execução em Termux
- Base para futuras arquiteturas Edge

---

## 🧠 Visão de Arquitetura

O sistema segue um design modular orientado a provedores:

````

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

### Conceitos-Chave

- **Dispatcher Pattern** — seleção dinâmica de provedores
- **Contratos de Interface** — garantem consistência
- **Azure-first** — pronto para serviços cognitivos
- **Fallback local** — permite testes offline
- **CLI minimalista** — automação-friendly

---

## ☁️ Integração com Azure

Os providers Azure utilizam variáveis de ambiente:

```bash
AZURE_TRANSLATOR_ENDPOINT=
AZURE_TRANSLATOR_KEY=
AZURE_TRANSLATOR_REGION=
````

Execução:

```bash
python main.py translate "Hello world" --provider azure
```

---

## 📱 Suporte Mobile (Termux)

Funciona diretamente em Termux:

```bash
pkg install python
pip install -r requirements.txt
python main.py translate "Edge computing é poderoso"
```

---

## ▶️ Uso

### Tradução

```bash
python main.py translate "Cloud systems scale fast" --source en --target pt
```

### Transliteração

```bash
python main.py transliterate "こんにちは" ja Latn
```

### Provider por variável de ambiente

```bash
export PROVIDER=local
python main.py translate "Cloud native platforms"
```

---

## 🛣️ Roadmap

**v1.0 — MVP do Bootcamp**

* CLI funcional
* Transliteration pipeline
* Providers Azure prontos
* Multi-engine
* Compatível com Termux

**v2.0 — Evolução Edge**

* Integração com Skuld MCP
* Execução como daemon mobile
* API REST
* Agentes orquestrados
* Control-plane distribuído

---

## 🧩 Inspiração Arquitetural

Este projeto se inspira em sistemas de orquestração Edge para ambientes mobile, demonstrando como serviços de IA em nuvem podem ser integrados em dispositivos portáteis.

---

## 📜 Licença

Uso educacional / open source.

---

## 👤 Autor

Desenvolvido para o desafio Microsoft Azure AI Bootcamp.

**AMJR**
