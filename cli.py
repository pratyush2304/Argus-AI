import sys
from bot_core import ChatEngine


def main():
    try:
        engine = ChatEngine()
    except ValueError as err:
        sys.exit(
            f"\n[Error]: {err}\n"
            "Create a .env file containing: GROQ_API_KEY=your_key\n"
        )

    print("==================================================")
    print("             Groq Python AI Chatbot")
    print("==================================================")
    print(f"Model: {engine.model}")
    print("Type 'exit', 'quit', or 'reset' at any time.")
    print("==================================================\n")

    while True:
        try:
            user_input = input("You > ").strip()

            if not user_input:
                continue

            if user_input.lower() in ("exit", "quit"):
                print("\nGoodbye!")
                break

            if user_input.lower() == "reset":
                engine.reset_chat()
                print("\n[Chat context reset]\n")
                continue

            print("\nBot > ", end="", flush=True)

            for token in engine.send_message_stream(user_input):
                print(token, end="", flush=True)

            print("\n")

        except KeyboardInterrupt:
            print("\n\nSession terminated.")
            break

        except Exception as e:
            print(f"\n[Groq API Error]: {e}\n")


if __name__ == "__main__":
    main()
