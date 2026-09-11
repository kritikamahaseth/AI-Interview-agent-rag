**Project Overview**
<br>
This project is an **AI-powered interview assistant** that can conduct adaptive technical and behavioral interviews. It is designed to evaluate candidate answers using a combination of:
<br>
**FAISS-based** retrieval of domain-specific knowledge
<br>
**OpenAI LLM evaluation** for scoring, strengths/weaknesses, and improvement suggestions
<br>
Currently, due to **API quota limitations**, the project uses a **dummy evaluation** to simulate LLM feedback.
<br>
**Project Structure**<br>
ai-interview-agent/<br>
│<br>
├─ app.py                # Main FastAPI application<br>
├─ knowledge_base.py     # Contains curated domain knowledge<br>
├─ questions.py          # List of interview questions<br>
├─ build_faiss_index.py  # Builds FAISS index from knowledge base<br>
├─ faiss_index.index     # Pre-built FAISS index for retrieval<br>
├─ requirements.txt      # Python dependencies<br>
└─ venv/                 # Virtual environment (excluded from GitHub)<br>
<br>
**Key Concepts**<br>
**1. Question**<br>

The interview question posed to the candidate.<br>
Example: "What is machine learning?"<br>

**2. Candidate Answer**<br>

The response given by the candidate.<br>
Example: "Learns from data."<br>

**3. FAISS / Knowledge Retrieval**<br>

FAISS retrieves the most relevant knowledge snippets from the knowledge base for a given question.<br>

Example retrieved context for "What is machine learning?":<br>
- Supervised learning is a machine learning approach where models are trained using labeled data.<br>
- A neural network is a model inspired by the human brain that learns complex patterns.<br>

**Role:** **FAISS is the reference lookup** :it finds the knowledge the candidate answer will be evaluated against.<br>

**4. OpenAI (Optional LLM Evaluation)** <br>

OpenAI reads the candidate answer + retrieved context and generates:<br>
Score (0–10)<br>
Strengths<br>
Weaknesses<br>
Suggestions for improvement<br>

**Role**: **OpenAI** **is the intelligent grader and explainer**, deciding how good the answer is and giving feedback.<br>

**Interview flow:** <br>
Candidate sees question<br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         ↓<br>
Candidate types answer<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ↓<br>
FAISS retrieves relevant knowledge from KB<br>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         ↓<br>
OpenAI (LLM) evaluates answer using retrieved knowledge<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          ↓<br>
Returns score, strengths, weaknesses, suggestions<br>

**Notes:** <br>

FAISS = deterministic, reliable retrieval <br>

OpenAI = probabilistic, intelligent evaluation <br>

Currently, dummy evaluation is used in place of OpenAI due to API quota limits <br>

**Components Overview** <br>
Candidate:	Provides answers to interview questions. <br>
Question:	Interview prompt displayed to candidate. <br>
Knowledge Base:	Curated domain-specific knowledge (questions, explanations, examples). <br>
FAISS:	Retrieves the most relevant knowledge snippets based on the question or candidate answer. <br>
Evaluation Layer:	Assesses candidate answer using retrieved context. Can be OpenAI LLM or dummy evaluation. <br>
FastAPI Server:	Handles requests, runs retrieval & evaluation, and returns structured feedback. <br>

**Architecture** <br><br>
<img width="417" height="702" alt="image" src="https://github.com/user-attachments/assets/2eb40738-1fbf-471c-933b-84180808f8f1" />


