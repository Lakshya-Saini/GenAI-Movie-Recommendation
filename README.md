# Movie & TV Show Recommendation App 🎬🍿

## Description

The **Movie & TV Show Recommendation App** is platform designed to provide personalized movie and TV show recommendations using **Generative AI (GenAI)**. The app leverages advanced AI models and APIs to deliver tailored recommendations based on user preferences, custom queries, and streaming availability. The backend is powered by Python, while the frontend is built using **Streamlit** for a seamless and interactive user experience. The app integrates with the **TMDB API** to fetch movie and TV show data, and uses **OpenAI** and **HuggingFace** models to generate intelligent recommendations and explanations.

---

## Features

- **Personalized Recommendations**:

  - Get recommendations based on selected preferences such as **movie/TV show type**, **genres**, and **streaming availability**.
  - Custom recommendations based on **user-provided preferences** (e.g., "Show me thrillers from the 90s").

- **Powered by GenAI**:

  - Uses **OpenAI** and **HuggingFace** models to generate intelligent and context-aware recommendations.
  - Provides **"Why is it worth watching?"** explanations for each recommendation.

- **Dynamic Query Generation**:

  - Converts user preferences into optimized **TMDB API queries** to fetch relevant data.

## Tech Stack

- **Frontend**: Streamlit (for a lightweight and interactive UI).
- **Backend**: Python
- **GenAI Integration**: OpenAI GPT, Hugging Face Transformers.
- **Data Source**: TMDB API (for movie/TV show data).

---

## How It Works

1. **User Provides Preferences**:

   - Users select their preferences (e.g., genres, streaming platforms) or type custom queries.

2. **LLM Generates TMDB API Query**:

   - The app uses **Generative AI** to convert user preferences into optimized TMDB API queries.

3. **Fetch Data from TMDB API**:

   - The app fetches movie/TV show data from the TMDB API based on the generated query.

4. **Format and Display Recommendations**:

   - The fetched data is formatted and displayed with details
   - GenAI generates a **"Why is it worth watching?"** explanation for each recommendation.

---

## How to Setup

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone git@github.com:Lakshya-Saini/GenAI-Movie-Recommendation.git
```

### 2. Create virtual env

```bash
python -m venv .venv
```

### 3. Activate virtual env

#### 3.a. For mac

```bash
source .venv/bin/activate
```

#### 3.b. For windows

```bash
.\.venv\Scripts\Activate.ps1
```

### 4. Copy .env.local to .env and Add your API keys

```bash
cp .env.local .env
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run app

```bash
streamlit run src/main.py
```

The app will be running at: http://localhost:8501
