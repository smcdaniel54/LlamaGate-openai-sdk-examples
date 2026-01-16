# LlamaGate OpenAI SDK Examples

Complete examples and tutorial for using the official OpenAI Python SDK with [LlamaGate](https://github.com/smcdaniel54/LlamaGate). Learn how to connect your OpenAI SDK code to local LLMs running on Ollama with zero code changes.

## Overview

This repository provides working examples and a step-by-step guide for using the official OpenAI Python SDK with LlamaGate, an OpenAI-compatible API gateway that serves as a drop-in replacement for connecting to local LLMs (Ollama). 

By simply configuring the SDK's `base_url` parameter to point at LlamaGate, you can use your existing OpenAI SDK code without any modifications. LlamaGate handles the translation between OpenAI's API format and Ollama's local endpoints, making it seamless to switch between OpenAI's cloud services and local models.

**What you'll learn:**
- How to configure the OpenAI SDK to work with local LLMs
- Non-streaming and streaming (SSE) chat completion examples
- Error handling patterns for local LLM development
- Best practices for using Ollama models with OpenAI-compatible APIs

The examples below demonstrate both non-streaming and streaming chat completions using the OpenAI SDK configured to use LlamaGate as the backend.

## Installation

```bash
pip install openai
```

Ensure LlamaGate is running and accessible at `http://localhost:11435/v1`.

**Note:** LlamaGate requires you to specify a model in each request (it does not have a default model). This project uses `"mistral"` (Mistral 7B) as the default model in all examples, matching LlamaGate's recommended default (works on CPU-only or 8GB VRAM). Replace it with any model available in your Ollama installation (e.g., `llama3`, `llama3.2`, `codellama`). To see available models, run `ollama list`. To pull a model, run `ollama pull <model-name>`.

## Examples

### Non-Streaming Example

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11435/v1",
    api_key="not-needed"  # If you enable LlamaGate API-key auth, set api_key=... accordingly
)

response = client.chat.completions.create(
    model="mistral",
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
    api_key="not-needed"  # If you enable LlamaGate API-key auth, set api_key=... accordingly
)

stream = client.chat.completions.create(
    model="mistral",
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
    api_key="not-needed"  # If you enable LlamaGate API-key auth, set api_key=... accordingly
)

try:
    response = client.chat.completions.create(
        model="mistral",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response.choices[0].message.content)
except APIError as e:
    print(f"API Error: {e.status_code} - {e.message}")
except Exception as e:
    print(f"Error: {e}")
```

## Why LlamaGate

LlamaGate enables you to use the familiar OpenAI SDK interface with local models running via Ollama. This provides a consistent development experience whether you're prototyping with local models or deploying with cloud services.

**Key benefits:**
- **Zero code changes**: Use your existing OpenAI SDK code as-is
- **Local development**: Test and develop with local LLMs without API costs
- **Privacy**: Keep your data local with on-premise model inference
- **Flexibility**: Easily switch between local and cloud models
- **Open source**: Full control over your LLM infrastructure

Perfect for developers who want to prototype locally, reduce API costs, maintain data privacy, or build applications that work with both local and cloud-based LLM services.
