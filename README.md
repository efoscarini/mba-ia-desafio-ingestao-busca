# Desafio MBA Engenharia de Software com IA - Full Cycle

## Ingestao e Busca Semantica com LangChain e PostgreSQL (pgVector)

Software que realiza ingestao de um PDF em um banco vetorial (PostgreSQL + pgVector) e permite busca semantica via CLI utilizando LangChain e OpenAI.

## Pre-requisitos

- Python 3.10+
- Docker e Docker Compose
- Chave de API da OpenAI

## Configuracao

1. Copie o arquivo `.env.example` para `.env` e preencha sua chave da OpenAI:

```bash
cp .env.example .env
```

Edite o `.env` e insira sua `OPENAI_API_KEY`:

```
OPENAI_API_KEY=sk-...
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
OPENAI_LLM_MODEL=gpt-5-nano
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag
PG_VECTOR_COLLECTION_NAME=pdf_documents
PDF_PATH=document.pdf
```

2. Crie e ative o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependencias:

```bash
pip install -r requirements.txt
```

## Execucao

### 1. Subir o banco de dados

```bash
docker compose up -d
```

Aguarde o container ficar healthy (o bootstrap criara a extensao `vector` automaticamente).

### 2. Executar a ingestao do PDF

```bash
python src/ingest.py
```

Isso ira:
- Carregar o PDF (`document.pdf`)
- Dividir em chunks de 1000 caracteres com overlap de 150
- Gerar embeddings via OpenAI (`text-embedding-3-small`)
- Armazenar os vetores no PostgreSQL com pgVector

### 3. Rodar o chat

```bash
python src/chat.py
```

Digite suas perguntas e receba respostas baseadas no conteudo do PDF. Digite `sair` para encerrar.

### Exemplo de uso

```
Chat iniciado! Digite 'sair' para encerrar.

PERGUNTA: Qual o faturamento da Empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhoes de reais.

PERGUNTA: Qual e a capital da Franca?
RESPOSTA: Nao tenho informacoes necessarias para responder sua pergunta.

PERGUNTA: sair
Encerrando chat. Ate logo!
```

## Estrutura do projeto

```
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── src/
│   ├── ingest.py         # Script de ingestao do PDF
│   ├── search.py         # Busca semantica + LLM
│   ├── chat.py           # CLI para interacao com usuario
├── document.pdf          # PDF para ingestao
└── README.md
```

## Tecnologias

- **Python** + **LangChain**
- **PostgreSQL** + **pgVector** (via Docker)
- **OpenAI** (embeddings: `text-embedding-3-small`, LLM: `gpt-5-nano`)