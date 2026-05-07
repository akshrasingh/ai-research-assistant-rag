import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def rewrite_query(query):

    prompt = f"""
    Rewrite the following query
    to make it more specific
    and optimized for document retrieval.

    Query:
    {query}

    Rewritten Query:
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return data["response"].strip()