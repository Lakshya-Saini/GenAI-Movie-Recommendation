from models.openai import call_openai
from models.huggingface import call_huggingface_inference_client

def call_model(model, model_type, user_prompt, system_prompt):
    if model_type == "huggingface":
        return call_huggingface_inference_client(model, user_prompt, system_prompt)
    elif model_type == "openai":
        return call_openai(user_prompt, system_prompt, model)
    else:
        raise ValueError("Invalid model type. Please provide a valid model type (huggingface or openai).")
