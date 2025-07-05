import ollama

class OllamaChatClient:
    def __init__(self, model: str):
        self.model = model

    def chat(self, system_prompt: str, user_prompt: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        response = ollama.chat(model=self.model, messages=messages)
        return response['message']['content']

if __name__ == "__main__":
    # ...existing code...
    MODEL = "llama3.2"
    system_prompt = "System prompt: You are a helpful assistant."
    user_prompt = "Who is Virat Kohli?"
    client = OllamaChatClient(MODEL)
    reply = client.chat(system_prompt, user_prompt)
    print("Ollama response:", reply)

