# Project Setup

1. Open Anaconda PowerShell.
2. Navigate to the folder where you cloned this repository:

# Project Setup

1. Open Anaconda PowerShell.
2. Navigate to the folder where you cloned this repository:

This will create a conda environment called `llms` with all the dependencies installed.
4. Activate the environment:

5. After activating the environment, start Jupyter Lab with:

# LLM Playground

## Setup Ollama and Pull Model

1. Download and install [Ollama](https://ollama.com/download).
2. Open a terminal and run the following command to pull the llama3.2 model:
   ```
   ollama pull llama3.2
   ```

## Interact with Ollama using Python

You can interact with Ollama directly using Python's `requests` library or the `ollama` package.

### Using python requests to interact with Ollama's chat API

```python
import requests
OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

messages = [
    {"role": "user", "content": "Describe some of the business applications of Generative AI"}
]

payload = {
    "model": MODEL,
    "messages": messages,
    "stream": False
}

response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
print(response.json()['message']['content'])
```

### ollama package alternative

```python
import ollama

MODEL = "llama3.2"
messages = [
    {"role": "user", "content": "Describe some of the business applications of Generative AI"}
]

response = ollama.chat(model=MODEL, messages=messages)
print(response['message']['content'])
```