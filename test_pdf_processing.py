from backend.ingestion.loader import load_pdf
from backend.ingestion.splitter import split_documents
from backend.vectorstore.faiss_store import create_vectorstore


PDF_PATH = "data/uploads/sample.pdf"


def main():
    print("Loading PDF...")

    documents = load_pdf(PDF_PATH)

    print(f"Pages loaded: {len(documents)}")

    print("\nSplitting document...")

    chunks = split_documents(documents)

    print(f"Chunks created: {len(chunks)}")

    print("\nCreating FAISS vector store...")

    vectorstore = create_vectorstore(chunks)

    print("FAISS vector store created successfully!")

    print("\nTesting similarity search...")

    results = vectorstore.similarity_search(
        "What programming skills does Klea have?",
        k=2
    )

    print(f"Results found: {len(results)}")

    for i, result in enumerate(results, start=1):
        print(f"\nResult {i}:")
        print("-" * 50)
        print(result.page_content[:500])
        print("\nMetadata:")
        print(result.metadata)


if __name__ == "__main__":
    main()
