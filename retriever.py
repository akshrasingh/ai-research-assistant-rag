import pickle
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, k=3):

    with open("faiss_store.pkl", "rb") as f:
        index, documents = pickle.load(f)

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, k)

    results = [documents[i] for i in indices[0]]

    return results