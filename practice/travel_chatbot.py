import os
from openai import OpenAI


def get_openai_client():
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )


MODEL = "deepseek/deepseek-r1-distill-llama-70b:free"

system_message = (
    "You are a helpful assistant for an Travel across India called TravelAI. "
    "Give short, courteous answers, no more than 1 sentence. "
    "Always be accurate. If you don't know the answer, say so."
)

openai = get_openai_client()


def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL, messages=messages)
    return response.choices[0].message.content


import gradio as gr

gr.ChatInterface(
    fn=chat,
    title="✈️ TravelAI Chatbot",
    description="Ask me anything about your travel!",
    type="messages"
).launch()
