import os
from dotenv import load_dotenv
from streamlit_ui.index import get_streamlit_ui
load_dotenv()

def run_app():
    model_type = "openai" # or "huggingface"
    huggingface_model = os.getenv("HUGGINGFACE_MODEL_NAME")
    openai_model = os.getenv("OPENAI_MODEL_NAME")
    hf_access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    tmdb_api_key = os.getenv("TMDB_API_SECRET_KEY")

    if (model_type == "huggingface") and (hf_access_token is None or hf_access_token == ""):
        raise ValueError("Please provide the Hugging Face api key in the .env file.")
    
    if (model_type == "openai") and (openai_api_key is None or openai_api_key == ""):
        raise ValueError("Please provide the OpenAI api key in the .env file.")
    
    if (tmdb_api_key is None or tmdb_api_key == ""):
        raise ValueError("Please provide the TMDB api key in the .env file.")

    get_streamlit_ui(model=openai_model, model_type="openai")


if __name__ == "__main__":
    app = run_app()