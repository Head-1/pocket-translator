# Pocket Translator — Documento de Arquitetura

## 1. Objetivo

Este documento descreve a arquitetura técnica do projeto Pocket Translator, um assistente linguístico baseado em CLI projetado para oferecer tradução e transliteração utilizando o Azure AI Translator e provedores alternativos.

O sistema é otimizado para portabilidade, extensibilidade e execução em ambientes móveis como Android via Termux.

---

## 2. Princípios de Design

- **Arquitetura orientada a provedores**
- **Cloud-first, compatível com Edge**
- **Contratos baseados em interfaces**
- **Execução local tolerante a falhas**
- **Interação CLI-first**
- **Configuração via variáveis de ambiente**

---

## 3. Visão Geral dos Componentes

### 3.1 Camada CLI

Responsável por:

- Interpretar comandos do usuário
- Exibir resultados
- Selecionar provedores
- Encaminhar requisições para o dispatcher

### 3.2 Dispatcher

Camada central de orquestração:

- Carrega provedores conforme configuração
- Roteia solicitações de tradução e transliteração
- Garante conformidade com interfaces

### 3.3 Camada de Provedores

Implementa a lógica específica de cada engine:

- Clientes REST do Azure Translator
- Motores locais de fallback
- Futuros serviços em nuvem

### 3.4 Módulo de Configuração

Responsável por carregar:

- seleção de provedores
- credenciais
- flags de execução

---

## 4. Fluxo de Execução

[Usuário / CLI]
|
v
[Dispatcher]
|
v
[Provider de Tradução / Transliteração]
|
v
[API Externa ou Engine]
|
v
[Resultado para a CLI]

---

## 5. Modelo de Integração com Azure

O Azure AI Translator é utilizado através de:

- Endpoints REST `/translate` e `/transliterate`
- Versão de API `3.0`
- Variáveis de ambiente para credenciais
- Roteamento baseado em região

A segurança é garantida por:

- Nenhuma chave no código-fonte
- Uso exclusivo de variáveis de ambiente
- Suporte a arquivos `.env`
- Modo de desenvolvimento local

---

## 6. Execução Mobile / Edge

O sistema é compatível com Termux:

- Ambientes virtuais Python
- Dependências leves
- Automação via CLI
- Provedores offline como fallback

Isso permite a criação de nós portáteis de tradução com suporte em nuvem.

---

## 7. Considerações de Segurança

- Chaves de API nunca versionadas
- Tokenização via ambiente
- Nenhuma porta exposta
- Superfície apenas CLI
- Compatível com túneis SSH

---

## 8. Estratégia de Extensibilidade

Novos provedores podem ser adicionados seguindo:

1. Implementar interfaces em `core/interfaces.py`
2. Criar um módulo de provider
3. Registrar no Dispatcher
4. Atualizar documentação

---

## 9. Roadmap Futuro (Pós-Bootcamp)

- Integração com Skuld MCP
- Modo daemon mobile
- Gateway REST
- Orquestração baseada em agentes
- Edge control-plane
- Pipelines de telemetria

---

## 10. Resumo

O Pocket Translator demonstra como serviços de IA cloud-native como o Azure AI Translator podem ser utilizados em ambientes móveis e edge por meio de uma arquitetura limpa, desacoplada e orientada a provedores.

---

**AMJR**

