import json
import os
from datetime import datetime

LOG_PATH = "backend/data/logs"
LOG_FILE = os.path.join(LOG_PATH, "traces.jsonl")

def log_trace(query, response, state):
    os.makedirs(LOG_PATH, exist_ok=True)

    record = {
        "time": datetime.utcnow().isoformat(),
        "query": query,
        "response": response,
        "state": state
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
