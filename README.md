# LlamaGate OpenAI SDK Examples

This repository demonstrates using the official OpenAI SDK with [LlamaGate](https://github.com/smcdaniel54/LlamaGate), an OpenAI-compatible API gateway that serves as a drop-in replacement for connecting to local LLMs (Ollama).

## Overview

This repository shows how to use the official OpenAI Python SDK with LlamaGate. By configuring the SDK's `base_url` parameter to point at LlamaGate, you can use existing OpenAI SDK code without modification. LlamaGate handles the translation between OpenAI's API format and Ollama's local endpoints, making it seamless to switch between OpenAI's cloud services and local models.

The examples below demonstrate both non-streaming and streaming (SSE) chat completions using the OpenAI SDK configured to use LlamaGate as the backend.

## Installation

```bash
pip install openai
```

Ensure LlamaGate is running and accessible at `http://localhost:11435/v1`.

**Note:** Replace `"llama3"` in the examples below with any model available in your Ollama installation (e.g., `llama3.2`, `mistral`, `codellama`). To see available models, run `ollama list`. To pull a model, run `ollama pull <model-name>`.

## Examples

### Non-Streaming Example

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11435/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="llama3",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
```

### Streaming Example

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11435/v1",
    api_key="not-needed"
)

stream = client.chat.completions.create(
    model="llama3",
    messages=[
        {"role": "user", "content": "Write a short poem about coding."}
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

See `example.py` for complete runnable examples.

### Error Handling Example

```python
from openai import OpenAI, APIError

client = OpenAI(
    base_url="http://localhost:11435/v1",
    api_key="not-needed"
)

try:
    response = client.chat.completions.create(
        model="llama3",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response.choices[0].message.content)
except APIError as e:
    print(f"API Error: {e.status_code} - {e.message}")
except Exception as e:
    print(f"Error: {e}")
```

## Why LlamaGate

LlamaGate enables you to use the familiar OpenAI SDK interface with local models running via Ollama. This provides a consistent development experience whether you're prototyping with local models or deploying with cloud services. For more information, visit the [LlamaGate repository](https://github.com/smcdaniel54/LlamaGate).
