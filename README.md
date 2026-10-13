# PDF RAG Chatbot — Work in Progress

A Python project exploring PDF retrieval as the foundation of a Retrieval-Augmented Generation (RAG) chatbot.

## Current status

Implemented: PDF loading, text chunking, local embeddings, FAISS indexing, retrieval and prompt preparation. LLM integration and a user interface are not implemented yet. The current output is retrieved context and a formatted prompt, not a generated answer.

## Pipeline

PDF → PyPDFLoader → text chunks → Hugging Face embeddings → FAISS → retriever → context → prompt

- Embedding model: `sentence-transformers/all-MiniLM-L6-v2`
- Chunk size: 1,000 characters; overlap: 200 characters
- Retriever: top 3 matching chunks
- Page labels are included when available in the PDF metadata.

## Project structure

```text
backend/
  ingestion/    # PDF loader, splitter and embeddings
  vectorstore/  # Create and save the FAISS index
  rag/          # Retriever, prompt template and context preparation
tests/          # Manual smoke-test scripts
requirements.txt
```

## Run locally

From the project root, with Python installed:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Create `data/uploads/` and place your own text-based PDF there as `sample.pdf`. No personal PDF or prebuilt index is included in this repository.

Run these scripts in order:

```powershell
.venv\Scripts\python.exe -m tests.test_pdf_processing
.venv\Scripts\python.exe -m tests.test_retriever
.venv\Scripts\python.exe -m tests.test_chain
```

The first script builds `vectorstore/faiss_index/`. The next two load that index. The first embedding-model download requires internet access; embeddings then run locally. Adjust the question in the scripts to match your PDF.

These scripts print results for manual inspection; they are not an automated assertion-based test suite. Dependencies are not version-pinned, so compatibility can vary between installations.

## Data handling

PDFs and generated indexes are excluded from version control. The index can contain source-document text. Load only indexes you created yourself: the current FAISS loader enables pickle deserialization.

## Planned improvements

- Integrate a cloud LLM to generate answers from the retrieved context.
- Add a user interface for document upload and questions.
- Add automated checks for retrieval and missing-document behavior.
- Pin and verify dependency versions in a fresh environment.

## Author

Klea Picalli
