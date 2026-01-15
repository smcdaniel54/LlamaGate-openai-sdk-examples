"""
LlamaGate OpenAI SDK Examples

This script demonstrates using the official OpenAI SDK with LlamaGate.
Ensure LlamaGate is running at http://localhost:11435/v1 before running.

Note: Replace "llama3" with any model available in your Ollama installation.
      Common models: llama3, llama3.2, mistral, codellama, etc.
      To see available models: ollama list
      To pull a model: ollama pull <model-name>
"""

from openai import OpenAI, APIError


def non_streaming_example():
    """Example of non-streaming chat completion."""
    print("=== Non-Streaming Example ===\n")
    
    try:
        response = client.chat.completions.create(
            model="llama3",
            messages=[
                {"role": "user", "content": "Hello, how are you?"}
            ]
        )
        
        print(f"Response: {response.choices[0].message.content}\n")
    except APIError as e:
        print(f"API Error: {e.status_code} - {e.message}\n")
        raise
    except Exception as e:
        print(f"Error: {e}\n")
        raise


def streaming_example():
    """Example of streaming chat completion (SSE)."""
    print("=== Streaming Example ===\n")
    
    try:
        stream = client.chat.completions.create(
            model="llama3",
            messages=[
                {"role": "user", "content": "Write a short poem about coding."}
            ],
            stream=True
        )
        
        print("Response: ", end="", flush=True)
        for chunk in stream:
            if chunk.choices and len(chunk.choices) > 0:
                delta = chunk.choices[0].delta
                if delta and delta.content is not None:
                    print(delta.content, end="", flush=True)
        print("\n")
    except APIError as e:
        print(f"API Error: {e.status_code} - {e.message}\n")
        raise
    except Exception as e:
        print(f"Error: {e}\n")
        raise


def error_handling_example():
    """Example of proper error handling."""
    print("=== Error Handling Example ===\n")
    
    try:
        response = client.chat.completions.create(
            model="nonexistent-model",
            messages=[
                {"role": "user", "content": "This will fail"}
            ]
        )
    except APIError as e:
        print(f"API Error caught:")
        print(f"  Status Code: {e.status_code}")
        print(f"  Message: {e.message}")
        print(f"  Type: {e.type}\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")


if __name__ == "__main__":
    # Configure client to use LlamaGate
    client = OpenAI(
        base_url="http://localhost:11435/v1",
        api_key="not-needed"
    )
    
    try:
        non_streaming_example()
        streaming_example()
        error_handling_example()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure LlamaGate is running at http://localhost:11435/v1")
        print("To check available models: ollama list")