from backend.rag.rag_engine import answer_query

tests = [
    ("what is the warranty of iphone 15", "warranty"),
    ("i want help with my order", "order"),
    ("1001", "order"),
    ("track my order", "Shipped"),
    ("what is ai", "I don't know"),
    ("refund my order", "refund"),
    ("what are your return policies", "return"),
    ("cancel my order 1002", "cannot"),
]

def run_tests():
    print("\n===== RUNNING SYSTEM EVALUATION =====\n")
    for q, expected in tests:
        out = answer_query(q)
        ok = expected.lower() in out.lower()
        print(f"Q: {q}")
        print(f"A: {out}")
        print(f"PASS: {ok}\n")

if __name__ == "__main__":
    run_tests()
