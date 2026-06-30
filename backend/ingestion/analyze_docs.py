with open("llms-full.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if line.startswith("# ") or line.startswith("## "):
            print(f"{i}: {line.strip()}")