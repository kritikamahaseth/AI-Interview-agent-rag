from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from questions import questions

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Extract reference answers from question bank
reference_answers = [q["reference_answer"] for q in questions]

# Convert answers to embeddings
embeddings = model.encode(reference_answers)

# Convert to numpy array
embeddings = np.array(embeddings).astype("float32")

# Get embedding dimension
dimension = embeddings.shape[1]

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Add embeddings to index
index.add(embeddings)


def search_answer(user_answer):
    """
    Takes user answer and returns the most similar reference answer
    """

    query_embedding = model.encode([user_answer])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, k=1)

    best_index = indices[0][0]
    best_answer = reference_answers[best_index]
    score = distances[0][0]

    return best_answer, score