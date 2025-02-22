import streamlit as st
import json
from models.huggingface import call_huggingface_inference_client
from models.openai import call_openai
from models.index import call_model
from prompts.index import get_prompt_for_tmdb_api, get_prompt_for_endpoint_extraction, get_prompt_for_response_format
from utils.filter import get_api_request
from tmdb_api.index import call_tmdb_api


def get_genres_list():
    return ["Action", "Comedy", "Drama", "Thriller", "Sci-Fi", "Horror", "Romance", "Documentary"]


def get_streaming_platforms_list():
    return ["Netflix", "Amazon Prime", "Hulu", "Disney+", "HBO Max"]


def get_preferences():
    col1, col2, col3 = st.columns([1, 2, 2])

    with col1:
        type = st.selectbox("Type", ["", "Movies", "TV Shows"], help="Choose between Movies and TV Shows")
    
    with col2:
        selected_genres = st.multiselect("Genres", get_genres_list(), help="Choose one or more genres")
    
    with col3:
        selected_streaming = st.multiselect("Streaming Availability", get_streaming_platforms_list(), help="Choose one or more streaming platforms")

    return type, selected_genres, selected_streaming


def get_user_input():
    col1 = st.columns(1)[0]

    with col1:
        user_input = st.text_input("Custom preferences", "")

    return user_input


def get_streamlit_ui(model, model_type):
    st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="wide")
    st.title("Movie Recommendation System")

    st.info(
        """
        NOTE: The data is fetched from TMDB API and the recommendations are generated using OpenAI's GPT-4o model. 
        The recommendations are based on your preferences and the latest data available on TMDB. The recommendations may not be 100% accurate everytime due to several factors
        including the availability of data, user preferences, and the model's predictions.
        """
    )

    st.subheader("Select your preferences to get movies and TV shows recommendations")
    type, selected_genres, selected_streaming = get_preferences()

    st.subheader("Or write your custom preferences here")
    user_input = get_user_input()

    # Process recommendations on button click
    if st.button("Get Recommendations"):
        if not any([type, selected_genres, selected_streaming, user_input]):
            st.error("Please select at least one preference.")
        else:
            # Process recommendations based on user preferences
            with st.spinner("Loading recommendations..."):
                if any([type, selected_genres, selected_streaming]):
                    # Create preferences dictionary if user has selected preferences
                    preferences_dict = {
                        "type": type,
                        "genres": selected_genres,
                        "streaming": selected_streaming
                    }
                    preferences_str = json.dumps(preferences_dict, indent=4)
                elif user_input:
                    # Use custom preferences if user has entered custom preferences
                    preferences_str = user_input

                # Call the model to get recommendations
                endpoint_response = call_model(model, model_type, preferences_str, get_prompt_for_tmdb_api())

                if endpoint_response == "Invalid query":
                    st.error("Please provide valid preferences.")
                    return

                # Extract API request from the response
                api_request = get_api_request(endpoint_response)
                if api_request:
                    endpoint = api_request
                else:
                    endpoint = call_model(model, model_type, endpoint_response, get_prompt_for_endpoint_extraction())
                
                # Call TMDB API to get recommendations
                response = call_tmdb_api(endpoint)

                if response and response.get('results') and len(response.get('results')) > 0:
                    # Get top 10 recommendations
                    response = response.get('results')[:10]

                    # check if endpoint has sort_by = vote_count, then sort the response by vote_average
                    if "sort_by=vote_count" in endpoint:
                        response = sorted(response, key=lambda x: x.get('vote_average'), reverse=True)

                    formatted_response = call_model(model, model_type, json.dumps(response), get_prompt_for_response_format())
                    st.write(formatted_response)
                else:
                    st.write("No recommendations found.")
