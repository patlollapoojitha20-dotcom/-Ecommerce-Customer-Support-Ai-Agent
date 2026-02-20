# 📦 Ecom Assist AI – Intelligent E-commerce Support Agent

Ecom Assist AI is a production-grade e-commerce support system built using FastAPI, OpenAI, LangChain, FAISS, and tool-based agents.

It combines deterministic agents (orders & payments) with Retrieval-Augmented Generation (RAG) to deliver accurate, safe, and scalable customer support.

This is NOT a toy chatbot.  
Financial and order logic is never hallucinated and is handled via tools, while static knowledge is served via RAG.

-------------------------------------------------------------------------------------------------------------------------------------------

## 📋 Table of Contents

- Quick Start – Setup & Run
- Overview
- Architecture & Workflow
- Project Structure
- API Keys & Environment Variables
- Backend Components
- Frontend Overview
- RAG System (Vector Store)
- Tool-Based Agents
- Sample Tool Data
- Running Tests
- Troubleshooting
- License

-------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Quick Start – Setup & Run

### Prerequisites

- Python 3.10+ (recommended 3.10 or 3.11)
- pip
- Virtual environment (recommended)
- OpenAI API key
- Node.js 18+ (for frontend)

-------------------------------------------------------------------------------------------------------------------------------------------

### Step 1: Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### Step 2: Install Backend Dependencies

```bash
pip install -r requirements.txt
```

Key libraries used:

- fastapi
- uvicorn
- langchain
- langchain-openai
- faiss-cpu
- python-dotenv
- pytest

### Step 3: Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

⚠️ Never commit .env files.

### Step 4: Build Vector Stores (ONE-TIME)

This embeds the knowledge base into FAISS vector stores.

```bash
python backend/rag/embeddings.py
```

Expected output:

```
✅ Embedded X chunks → backend/data/vector_store/policies
✅ Embedded X chunks → backend/data/vector_store/products
✅ Embedded X chunks → backend/data/vector_store/faqs
```

### Step 5: Run the Backend API

```bash
uvicorn backend.api.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

### Step 6: Run the Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:3000
```

### Step 7: Run Tests

```bash
pytest -v
```

-------------------------------------------------------------------------------------------------------------------------------------------

## 🎯 Overview

Ecom Assist AI is designed as a real-world e-commerce support backend.

It supports:

- Order tracking, cancellation, returns, refunds
- Payment handling (online, COD, failures, refunds)
- Policy, product, and FAQ queries via RAG
- Tool-based agent reasoning (Agent 2.0 architecture)
- Clear routing, logging, and explainability

---

## 🏗️ Architecture & Workflow

### High-Level Flow

```
User (Frontend)
   |
   ▼
FastAPI API (/chat)
   |
   ▼
Intent Detection (Semantic)
   |
   ├── Policy / Product / FAQ ──▶ RAG (FAISS + OpenAI)
   |
   ├── Order Actions ───────────▶ Order Agent Tools
   |
   └── Payment Queries ─────────▶ Payment Agent Tools
```

### System Architecture

```
┌──────────────────────────┐
│        Frontend UI       │
│ (React / Next.js / Web)  │
│                          │
│ - Chat interface         │
│ - Sends user messages    │
│ - Displays responses     │
└───────────┬──────────────┘
            │ HTTP POST /chat
            │
┌───────────▼──────────────┐
│      FastAPI Backend     │
│   backend/api/main.py    │
│                          │
│ - API Gateway            │
│ - Request validation     │
│ - Calls answer_query()   │
└───────────┬──────────────┘
            │
┌───────────▼──────────────────────────────────────────┐
│                Core Intelligence Layer               │
│              backend/rag/rag_engine.py               │
│                                                      │
│  Intent Detection (Semantic + Examples)              │
│                                                      │
│  ┌──────────────────────┐   ┌──────────────────────┐ │
│  │   Tool-Based Agents  │   │        RAG System    │ │
│  │ (Deterministic Logic)│   │ (FAISS + OpenAI LLM) │ │
│  │                      │   │                      │ │
│  │ Order Agent          │   │ Policy Vector Store  │ │
│  │ Payment Agent        │   │ Product Vector Store │ │
│  │                      │   │ FAQ Vector Store     │ │
│  └──────────┬───────────┘   └──────────┬───────────┘ │
│             │                          │             │
│  ┌──────────▼──────────┐   ┌───────────▼───────────┐ │
│  │ Tool Data (JSON)    │   │ Knowledge Base (.txt) │ │
│  │ sample_orders.json  │   │ policies/             │ │
│  │ payments.json       │   │ products/             │ │
│  └─────────────────────┘   │ faqs/                 │ │
│                            └───────────────────────┘ │
│                                                      │
│  Logging & Observability                             │
│  backend/core/logger.py                              │
└──────────────────────────────────────────────────────┘
```

-------------------------------------------------------------------------------------------------------------------------------------------

## 📁 Project Structure

```
ecom-assist/
├── backend/
|   |
|   ├──main.py
|   |
│   ├── api/
│   │   └── main.py
│   │
│   ├── rag/
│   │   ├── rag_engine.py
│   │   └── embeddings.py
│   │
│   ├── core/
│   │   └── logger.py
│   │
│   └── data/
│       ├── knowledge_base/
│       │   ├── policies/
│       │   ├── products/
│       │   └── faqs/
│       │
│       ├── vector_store/
│       │   ├── policies/
|       |   |      ├──index.faiss
|       |   |      ├──index.pkl
|       |   |  
│       │   ├── products/
|       |   |      ├──index.faiss
|       |   |      ├──index.pkl
│       │   └── faqs/
|       |          ├──index.faiss
|       |          ├──index.pkl
│       │
│       └── tool_data/
│           ├── sample_orders.json
│           └── payments.json
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.tsx
│   │   ├── index.css
|   |   └──main.tsx
|   |     
│   ├── index.html
│   └── README.md
│
├── tests/
│   └── test_order_agent.py
│
├── requirements.txt
├── .env.example
└── README.md
```

-------------------------------------------------------------------------------------------------------------------------------------------

## 🔑 API Keys & Configuration

**Required:**

- OpenAI API Key

**Used for:**

- Embeddings (text-embedding-3-large)
- LLM responses (gpt-4.1)

-------------------------------------------------------------------------------------------------------------------------------------------

## 🔧 Backend Components

### FastAPI (main.py)

- Single `/chat` endpoint
- Accepts user queries
- Routes to `answer_query()`

### RAG Engine (rag_engine.py)

Handles:

- Intent detection
- RAG routing
- Order agent
- Payment agent
- Tool execution
- Session memory
- Logging

-------------------------------------------------------------------------------------------------------------------------------------------

## 🎨 Frontend Overview

The frontend is a thin client.

It only does:

- Collect user messages
- Send requests to `/chat`
- Display responses

It does NOT handle:

- Intent detection
- RAG
- Order logic
- Payment logic

-------------------------------------------------------------------------------------------------------------------------------------------

## 📚 RAG System

**Knowledge Base:**

```
backend/data/knowledge_base/
```

**Vector Store:**

```
backend/data/vector_store/
```

Each category has its own FAISS index.

-------------------------------------------------------------------------------------------------------------------------------------------

## 🤖 Tool-Based Agents (Agent 2.0)

**Order Agent Tools:**

- `order_info_tool`
- `track_order_tool`
- `cancel_order_tool`
- `return_order_tool`
- `refund_order_tool`

**Payment Agent Tool:**

- `payment_status_tool`

**Why tools?**

- Deterministic
- Auditable
- Financially safe
- Interview-grade architecture

-------------------------------------------------------------------------------------------------------------------------------------------

## 💳 Sample Payment Tool Data

File: `backend/data/tool_data/payments.json`

```json
{
  "1001": {
    "payment_method": "online",
    "status": "success",
    "amount": 79900,
    "receipt_generated": true,
    "refund_initiated": false
  },
  "1002": {
    "payment_method": "cash_on_delivery",
    "status": "pending",
    "amount": 1599,
    "receipt_generated": false,
    "refund_initiated": false
  },
  "1003": {
    "payment_method": "online",
    "status": "failed",
    "amount": 2999,
    "receipt_generated": false,
    "refund_initiated": true
  }
}
```

-------------------------------------------------------------------------------------------------------------------------------------------

## 🧪 Running Tests

```bash
pytest -v
```

-------------------------------------------------------------------------------------------------------------------------------------------

## 🐛 Troubleshooting

- Rebuild vectors if RAG misbehaves
- Ensure `.txt` files are UTF-8 encoded
- Orders mutate during runtime (expected)
- Ensure order IDs exist in tool data

-------------------------------------------------------------------------------------------------------------------------------------------

## 🧠 Interview Explanation (One Line)

"We use tool-based agents for deterministic order and payment logic, while RAG is strictly limited to static knowledge like policies and products, preventing hallucination and ensuring safety."

-------------------------------------------------------------------------------------------------------------------------------------------

## 📝 License

This project is for educational and demonstration purposes.  
Check individual libraries for their licenses.

