import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from knowledge_base import knowledge

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Encode all knowledge
embeddings = model.encode(knowledge)
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)  # using L2 distance
index.add(embeddings)

# Save index
faiss.write_index(index, "faiss_index.index")

print("FAISS index created and saved!")