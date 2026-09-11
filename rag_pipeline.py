from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_knowledge_base():
    questions = []
    answers = []

    with open("knowledge_base.txt", "r") as f:
        lines = f.readlines()

    for i in range(0, len(lines), 3):
        q = lines[i].replace("Question:", "").strip()
        a = lines[i+1].replace("Answer:", "").strip()

        questions.append(q)
        answers.append(a)

    return questions, answers


questions, answers = load_knowledge_base()

# Create embeddings
question_embeddings = model.encode(questions)


def retrieve_reference(question):

    query_embedding = model.encode([question])[0]

    similarities = np.dot(question_embeddings, query_embedding)

    index = np.argmax(similarities)

    return answers[index]


def evaluate_answer(candidate_answer, reference_answer):

    candidate_vec = model.encode([candidate_answer])[0]
    ref_vec = model.encode([reference_answer])[0]

    similarity = np.dot(candidate_vec, ref_vec)

    score = round(float(similarity) * 10, 2)

    if score > 8:
        feedback = "Strong answer. Covers key concept."
    elif score > 5:
        feedback = "Partially correct but missing some details."
    else:
        feedback = "Answer needs improvement."

    return score, feedback