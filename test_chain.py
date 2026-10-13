from backend.rag.chain import prepare_rag_prompt


def main():
    question = "What programming skills does Klea have?"

    print("Preparing RAG prompt...")
    print(f"\nQuestion: {question}")

    prompt = prepare_rag_prompt(question)

    print("\nRAG prompt created successfully!")
    print("\n" + "=" * 60)
    print("PROMPT")
    print("=" * 60)

    print(prompt.to_string())


if __name__ == "__main__":
    main()
    