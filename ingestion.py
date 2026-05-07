import os
import pickle
import faiss
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def ingest(folder_path):

    documents = []

    for filename in os.listdir(folder_path):

        if filename.endswith(".pdf"):

            pdf_path = os.path.join(folder_path, filename)

            reader = PdfReader(pdf_path)

            text = ""

            for page in reader.pages:
                extracted = page.extract_text()

                if extracted:
                    text += extracted

            chunk_size = 500

            for i in range(0, len(text), chunk_size):

                chunk = text[i:i+chunk_size]

                documents.append({
                    "text": chunk,
                    "source": filename
                })

    chunk_texts = [doc["text"] for doc in documents]

    embeddings = model.encode(chunk_texts)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    with open("faiss_store.pkl", "wb") as f:
        pickle.dump((index, documents), f)

    return "Multi-document ingestion complete"