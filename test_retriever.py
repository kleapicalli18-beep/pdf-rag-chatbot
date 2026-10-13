from backend.rag.retriever import get_retriever


def main():
    print("Loading FAISS retriever...")

    retriever = get_retriever(k=3)

    question = "What programming skills does Klea have?"

    print(f"\nQuestion: {question}")

    documents = retriever.invoke(question)

    print(f"\nRelevant chunks found: {len(documents)}")

    for i, document in enumerate(documents, start=1):
        print(f"\n--- Result {i} ---")
        print(document.page_content[:700])
        print("\nMetadata:")
        print(document.metadata)


if __name__ == "__main__":
    main()