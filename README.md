📦 Ecommerce Assist AI – Intelligent E-commerce Support Agent
----------------------------------------------------------------------------------
Ecom Assist AI is a production-grade e-commerce support system built using FastAPI, OpenAI, LangChain, FAISS, and tool-based agents.

It combines
- Tool-based agents for orders & payments
- RAG for policies and FAQs
This is NOT a toy chatbot.
Financial and order logic is never hallucinated and is handled via tools, while static knowledge is served via RAG.
************************************************************************************
📋 Table of Contents
------------------------------------------------------------------------------------ 
- Quick Start - Setup & Run
- Overview
- Architecture & Workflow
- Project Structure
- Backend Components
- Frontend Overview
- RAG System (Vector Store)
- Sample Tool Data
- Running Tests
- Troubleshooting
- License
***************************************************************************************
🚀 Quick Start - Setup & Run
---------------------------------------------------------------------------------------
Prerequisites
- Python 3.10+ (recommended 3.10 or 3.11)
- pip
- Virtual environment (recommended)
- OpenAI API key
- Node.js 18+ (for frontend)
*****************************************************************************************
## Step 1: Create Virtual Environment ##

```
python -m venv venv

#Windows
venv/Scripts/activate

#mac0S / Linux
source venv/bin/activate
```
## Step 2: Install Backend Dependencies ##
```
pip install - requirements.txt
```
Key Libraries Used:
- fastapi
- uvicorn
- python-dotenv
- pytest

## Step 3: Environment Variables ##
Create a ```.env``` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Step 4: Build Vector Stores(ONE-TIME) ##
This embeds the knowledge base into FAISS vector stores
```
python backend/rag/embeddings.py
```
Expected output:
```
✅ Embedded X chunks → backend/data/vector_store/policies
✅ Embedded X chunks → backend/data/vector_store/products
✅ Embedded X chunks → backend/data/vector_store/faqs
```

## Step 5: Run The Backend ##
```
uvicorn backend.api.main.app --reload
```
Backend runs at:
```
http://127.0.0.1:8000
```

## Step 6: Run The Frontend ##
```
cd frontend
npm install
npm run dev
```
Frontend runs at:
```
https://localhost:3000
```
## Step 7: Run Tests ##
```
pytest -v
```
*****************************************************************************
# 🎯 Overview #
Ecom Assist AI is designed as a real-world e-commerce support backend

It supports:
- Order tracking, cancellation,returns,refunds
- Payment handling(online,COD,failures,refunds)
- Policy,product,and FAQ queries via RAG
- Tool-based agent reasoning (Agent2.0 architecture)
- Clear routing,logging, and explainability
******************************************************************************
# 🏗️ Architecture & Workflow
## High-Level Flow ##
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
## Project Structure ##
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
************************************************************************************
# 🔧 Backend Components #
## FastAPI (main.py) ##
- Single ```/chat``` endpoint
- Accepts user queries
- Routes to ```answer_query()```
## RAG Engine (rag_engine.py) ##
Handles:
- Intent detection
- RAG routing
- Order agent
- Payment agent
- Tool execution
- Session memory
- Logging
*****************************************************************************************
# 🎨 Frontend Overview #
The frontend is a thin client.

It only does:

- Collect user messages
- Send requests to /chat
- Display responses

It does NOT handle:

- Intent detection
- RAG
- Order logic
- Payment logic
***********************************************************************************************
# 📚 RAG System #
## Knowledge Base: ##
```
backend/data/knowledge_base/
```
## Vector Store: ##
```
backend/data/vector_store/
```
Each category has its own FAISS index.
*************************************************************************************************
# 💳 Sample Payment Tool Data #
File: 
```
backend/data/tool_data/payments.json
```
```
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
**************************************************************************************************
# 🧪 Running Tests #
```
pytest -v
```
*******************************************************************************************************
# 🐛 Troubleshooting #
- Rebuild vectors if RAG misbehaves
- Ensure ```.txt``` files are UTF-8 encoded
- Orders mutate during runtime (expected)
- Ensure order IDs exist in tool data
********************************************************************************************************
# 🧠 Interview Explanation (One Line) #
```
We separate business-critical actions (orders, payments) into deterministic tools, while using RAG only for static knowledge retrieval, ensuring reliability, traceability, and safe responses.
```
*********************************************************************************************************
# 📝 License #
```
This project is released for educational and demonstration purposes.

You may use and modify it for learning or portfolio use.  
Please review the licenses of all external libraries before using in production.
```

