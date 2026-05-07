import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate(query, context_chunks):
    
    context = "\n".join(
    [doc["text"] for doc in context_chunks]
)
    prompt = f"""
    Answer ONLY using the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]