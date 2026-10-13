from pathlib import Path

from langchain_community.vectorstores import FAISS

from backend.ingestion.embeddings import get_embeddings


VECTORSTORE_PATH = Path("vectorstore/faiss_index")


def create_vectorstore(chunks):
    """
    Creates a FAISS vector store from document chunks.
    """

    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    VECTORSTORE_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    vectorstore.save_local(str(VECTORSTORE_PATH))

    return vectorstore