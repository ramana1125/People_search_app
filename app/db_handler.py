import os
import json
import chromadb
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.create_collection(name="profiles", metadata={"hnsw:space": "cosine"})

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "sample_profiles.json")

def load_profiles(filepath=DATA_PATH):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def populate_db():
    profiles = load_profiles()
    for idx, profile in enumerate(profiles):
        text = f"{profile['name']} {profile['location']} {profile['interests']} {profile['bio']}"
        emb = embedder.encode([text])[0]
        collection.add(
            ids=[str(idx)],
            embeddings=[emb],
            metadatas=[{
                "name": profile["name"],
                "location": profile["location"],
                "interests": profile["interests"],
                "bio": profile["bio"]
            }]
        )

def search_profiles(query: str, top_k: int = 5):
    emb = embedder.encode([query])[0]
    results = collection.query(query_embeddings=[emb], n_results=top_k)

    matches = []
    for metadata, score in zip(results["metadatas"][0], results["distances"][0]):
        matches.append((metadata, 1 - score))

    return matches

populate_db()
