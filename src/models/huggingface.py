import os
from huggingface_hub import InferenceClient

def call_huggingface_inference_client(model: str, user_query: str, system_prompt: str, max_length: int = 512, temperature: float = 0.2):
    access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
    
    # Initialize the InferenceClient
    client = InferenceClient(
        model=model,  # Model name from the Hugging Face Hub
        token=access_token,  # Your Hugging Face access token
    )

    # Combine the system prompt and user query
    input_text = f"User: {user_query}\n\nSystem:{system_prompt}\n\nAssistant:"

    # Generate the response using the InferenceClient
    response = client.text_generation(
        prompt=input_text,
        max_new_tokens=max_length,
        temperature=temperature,
        return_full_text=False,  # Only return the assistant's response
    )

    return response.strip()
