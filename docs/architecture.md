# Pocket Translator — Architecture Document

## 1. Purpose

This document describes the technical architecture of the Pocket Translator project, a CLI-based linguistic assistant designed to support translation and transliteration using Azure AI Translator and alternative providers.

The system is optimized for portability, extensibility, and mobile execution environments such as Android via Termux.

---

## 2. Design Principles

- **Provider-based Architecture**
- **Cloud-first, Edge-capable**
- **Interface-driven Contracts**
- **Fail-safe Local Execution**
- **CLI-first Interaction**
- **Environment-driven Configuration**

---

## 3. Component Overview

### 3.1 CLI Layer

Responsible for:

- Parsing user commands
- Rendering output
- Selecting providers
- Forwarding requests to the dispatcher

### 3.2 Dispatcher

Central orchestration layer:

- Loads provider based on configuration
- Routes translation and transliteration requests
- Enforces interface contracts

### 3.3 Provider Layer

Implements engine-specific logic:

- Azure Translator REST clients
- Local fallback engines
- Future cloud providers

### 3.4 Configuration Module

Loads:

- provider selection
- credentials
- runtime flags

---

## 4. Runtime Flow

```

[User / CLI]
|
v
[Dispatcher]
|
v
[Translator / Transliterator Provider]
|
v
[External Engine or API]
|
v
[Result to CLI]

```

---

## 5. Azure Integration Model

Azure AI Translator is implemented using:

- REST endpoints `/translate` and `/transliterate`
- API version `3.0`
- Environment variables
- Region-based routing

Security is enforced by:

- No secrets in code
- Environment variables
- .env support
- Local-first development mode

---

## 6. Mobile / Edge Execution

The system is compatible with Termux:

- Python virtual environments
- Lightweight dependencies
- CLI automation
- Offline fallback providers

This enables pocket-sized translation nodes capable of cloud-assisted linguistic processing.

---

## 7. Security Considerations

- API keys never committed
- Tokenization through environment variables
- No inbound ports required
- CLI-only surface
- Suitable for SSH tunnels or mobile execution

---

## 8. Extensibility Strategy

New providers can be added by:

1. Implementing interfaces in `core/interfaces.py`
2. Creating a provider module
3. Registering it in the Dispatcher
4. Updating documentation

---

## 9. Future Roadmap (Post-Bootcamp)

- Skuld MCP integration
- Mobile daemon mode
- REST gateway
- Agent-based orchestration
- Edge control-plane
- Telemetry pipelines

---

## 10. Summary

Pocket Translator demonstrates how cloud-native AI services such as Azure AI Translator can be embedded into mobile-friendly edge environments through clean architectural separation and provider-driven design.

---

**AMJR**
