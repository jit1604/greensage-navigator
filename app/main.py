from fastapi import FastAPI
from collections import Counter

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/echo")
def echo(text: str):
    c = Counter(text)
    return {"text": text, "length": len(text), "most_common_char": c.most_common(1)[0][0]}