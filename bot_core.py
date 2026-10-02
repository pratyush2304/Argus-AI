from groq import Groq
import config


class ChatEngine:
    def __init__(self, system_instruction: str = config.SYSTEM_INSTRUCTION):
        if not config.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY environment variable is missing.")

        self.client = Groq(api_key=config.GROQ_API_KEY)
        self.system_instruction = system_instruction
        self.model = config.DEFAULT_MODEL
        self.reset_chat()

    def reset_chat(self):
        """Clear conversation history and start a new conversation."""
        self.messages = [
            {
                "role": "system",
                "content": self.system_instruction,
            }
        ]

    def send_message_stream(self, message: str):
        """Send a message to Groq and stream the response."""
        self.messages.append({
            "role": "user",
            "content": message,
        })

        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=0.7,
                stream=True,
            )

            full_response = ""

            for chunk in stream:
                if not chunk.choices:
                    continue

                content = chunk.choices[0].delta.content

                if content:
                    full_response += content
                    yield content

            if full_response:
                self.messages.append({
                    "role": "assistant",
                    "content": full_response,
                })

        except Exception:
            if self.messages and self.messages[-1]["role"] == "user":
                self.messages.pop()
            raise
