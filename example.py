"""
LlamaGate OpenAI SDK Examples

This script demonstrates using the official OpenAI SDK with LlamaGate.
Ensure LlamaGate is running at http://localhost:11435/v1 before running.
"""

from openai import OpenAI

# Configure client to use LlamaGate
client = OpenAI(
    base_url="http://localhost:11435/v1",
    api_key="not-needed"
)


def non_streaming_example():
    """Example of non-streaming chat completion."""
    print("=== Non-Streaming Example ===\n")
    
    response = client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )
    
    print(f"Response: {response.choices[0].message.content}\n")


def streaming_example():
    """Example of streaming chat completion (SSE)."""
    print("=== Streaming Example ===\n")
    
    stream = client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "user", "content": "Write a short poem about coding."}
        ],
        stream=True
    )
    
    print("Response: ", end="", flush=True)
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")


if __name__ == "__main__":
    try:
        non_streaming_example()
        streaming_example()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure LlamaGate is running at http://localhost:11435/v1")
