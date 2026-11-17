import ollama


MODEL = "llama3.2"
MODEL_QWEN = "qwen2.5:0.5b"
EXIT_COMMANDS = {"exit", "quit", "q"}


def ask(model: str, history: list[dict]) -> str:
    """Send the conversation to the model and return its reply."""
    response = ollama.chat(model=model, messages=history)
    return response["message"]["content"]


def chat(model: str) -> None:
    """Run a simple terminal chat loop."""
    history: list[dict] = []
    print(f"Chatting with {model}. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in EXIT_COMMANDS:
            break

        history.append({"role": "user", "content": user_input})
        reply = ask(model, history)
        history.append({"role": "assistant", "content": reply})

        print(f"{model}: {reply}\n")


if __name__ == "__main__":
    chat(MODEL)

