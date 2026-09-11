# # OpenAI LLM evaluation is commented out due to API quota limits.
# # Dummy evaluation is used here for demonstration purposes.



# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # import faiss
# # import numpy as np
# # from sentence_transformers import SentenceTransformer
# # import os
# # from openai import OpenAI

# # from knowledge_base import knowledge
# # from questions import interview_questions

# # app = FastAPI()

# # # Load embedding model
# # model = SentenceTransformer("all-MiniLM-L6-v2")

# # # Load FAISS index
# # index = faiss.read_index("faiss_index.index")

# # # OpenAI client
# # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # class InterviewInput(BaseModel):
# #     question: str
# #     candidate_answer: str


# # def retrieve_context(query, k=2):
# #     query_vector = model.encode([query])
# #     distances, indices = index.search(np.array(query_vector).astype("float32"), k)

# #     context = []
# #     for idx in indices[0]:
# #         context.append(knowledge[idx])

# #     return "\n".join(context)


# # def evaluate_answer(question, candidate_answer, context):

# #     prompt = f"""
# # You are an AI technical interviewer.

# # Question:
# # {question}

# # Reference knowledge:
# # {context}

# # Candidate answer:
# # {candidate_answer}

# # Evaluate the answer.

# # Return:

# # Score (0-10)
# # Correctness
# # Strengths
# # Weaknesses
# # How to improve
# # """

# #     response = client.chat.completions.create(
# #         model="gpt-4o-mini",
# #         messages=[
# #             {"role": "system", "content": "You are an expert technical interviewer."},
# #             {"role": "user", "content": prompt}
# #         ],
# #         temperature=0.3
# #     )

# #     return response.choices[0].message.content


# # @app.post("/evaluate")
# # def evaluate(input: InterviewInput):

# #     context = retrieve_context(input.question)

# #     evaluation = evaluate_answer(
# #         input.question,
# #         input.candidate_answer,
# #         context
# #     )

# #     return {
# #         "question": input.question,
# #         "candidate_answer": input.candidate_answer,
# #         "evaluation": evaluation
# #     }
# from fastapi import FastAPI
# from pydantic import BaseModel
# import faiss
# import numpy as np
# from sentence_transformers import SentenceTransformer

# from knowledge_base import knowledge
# from questions import interview_questions

# app = FastAPI()

# # Load embedding model
# model = SentenceTransformer("all-MiniLM-L6-v2")

# # Load FAISS index
# index = faiss.read_index("faiss_index.index")


# class InterviewInput(BaseModel):
#     question: str
#     candidate_answer: str


# def retrieve_context(query, k=2):
#     """
#     Retrieve relevant knowledge snippets from FAISS index.
#     """
#     query_vector = model.encode([query])
#     distances, indices = index.search(np.array(query_vector).astype("float32"), k)

#     context = []
#     for idx in indices[0]:
#         context.append(knowledge[idx])

#     return "\n".join(context)


# def evaluate_answer(question, candidate_answer, context):
#     """
#     Dummy evaluation without OpenAI.
#     """
#     # This simulates what OpenAI would return
#     return (
#         f"Dummy evaluation:\n"
#         f"Candidate Answer: {candidate_answer}\n"
#         f"Context Retrieved: {context}\n"
#         f"Score (0-10): 7\n"
#         f"Strengths: Shows basic understanding\n"
#         f"Weaknesses: Lacks details/examples\n"
#         f"Improvement: Expand explanation with examples and technical terms"
#     )


# @app.post("/evaluate")
# def evaluate(input: InterviewInput):
#     try:
#         context = retrieve_context(input.question)
#         evaluation = evaluate_answer(
#             input.question,
#             input.candidate_answer,
#             context
#         )

#         return {
#             "question": input.question,
#             "candidate_answer": input.candidate_answer,
#             "evaluation": evaluation
#         }
#     except Exception as e:
#         # Return friendly error instead of 500
#         return {"error": str(e)}



from fastapi import FastAPI
from pydantic import BaseModel
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

# Uncomment if you have OpenAI quota
# from openai import OpenAI

from knowledge_base import knowledge
from questions import interview_questions

app = FastAPI()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("faiss_index.index")

# OpenAI client (commented due to quota)
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class InterviewInput(BaseModel):
    question: str
    candidate_answer: str

def retrieve_context(query, k=2):
    """
    Retrieve relevant knowledge snippets from FAISS index.
    """
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector).astype("float32"), k)

    context = []
    for idx in indices[0]:
        context.append(knowledge[idx])

    return "\n".join(context)

# Dummy evaluation (active)
def evaluate_answer(question, candidate_answer, context):
    """
    Dummy evaluation without OpenAI.
    Used for demonstration due to API quota limitations.
    """
    return {
        "candidate_answer": candidate_answer,
        "context_retrieved": context,
        "score": 7,
        "strengths": "Shows basic understanding",
        "weaknesses": "Lacks details/examples",
        "improvement": "Expand explanation with examples and technical terms"
    }
 
# OpenAI evaluation (commented)
"""
def evaluate_answer(question, candidate_answer, context):
    # Real LLM evaluation using OpenAI API
    prompt = f'''
You are an AI technical interviewer.

Question:
{question}

Reference knowledge:
{context}

Candidate answer:
{candidate_answer}

Evaluate the answer.

Return:

Score (0-10)
Correctness
Strengths
Weaknesses
How to improve
'''
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert technical interviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
"""

@app.post("/evaluate")
def evaluate(input: InterviewInput):
    try:
        context = retrieve_context(input.question)
        evaluation = evaluate_answer(
            input.question,
            input.candidate_answer,
            context
        )

        return {
            "question": input.question,
            "candidate_answer": input.candidate_answer,
            "evaluation": evaluation
        }
    except Exception as e:
        return {"error": str(e)}