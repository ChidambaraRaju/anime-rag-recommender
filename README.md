# 🎌 Anime Recommender System 🎨

This project is a RAG (Retrieval-Augmented Generation) based anime recommender system built using Langchain. It leverages the power of large language models (LLMs) to provide personalized anime recommendations based on user descriptions.

## ✨ Features

*   **Natural Language Input:** Describe the kind of anime you want to watch in plain English.
*   **Personalized Recommendations:** Get recommendations tailored to your specific preferences.
*   **Interactive UI:** A user-friendly web interface built with Streamlit.
*   **RAG-based:** Utilizes a Retrieval-Augmented Generation pipeline for accurate and context-aware recommendations.
*   **Vector Search:** Employs ChromaDB for efficient similarity search of anime synopses.

## 🚀 Technologies Used

*   **LangChain:** For building the RAG pipeline and orchestrating the LLM interactions.
*   **Streamlit:** To create the interactive web application.
*   **ChromaDB:** As the vector store for anime data.
*   **Groq:** For accessing the Llama 3 language model.
*   **Hugging Face Embeddings:** To generate embeddings for anime synopses.
*   **Docker:** For containerizing the application.
*   **Kubernetes:** For orchestrating the containerized application (as suggested by `llmops-k8s.yaml`).

## 🏗️ Architecture

The application follows a Retrieval-Augmented Generation (RAG) architecture:

1.  **Data Loading and Processing:** Anime data, including synopses, is loaded from a CSV file and processed.
2.  **Embedding Generation:** The synopses are converted into vector embeddings using a Hugging Face sentence transformer model.
3.  **Vector Storage:** The generated embeddings are stored in a ChromaDB vector store.
4.  **User Query:** The user provides a natural language query describing their desired anime.
5.  **Retrieval:** The user's query is converted into an embedding, and a similarity search is performed on the ChromaDB to retrieve the most relevant anime synopses.
6.  **Augmentation:** The retrieved synopses are then used as context for the LLM.
7.  **Generation:** The LLM (Llama 3 via Groq) generates a personalized recommendation based on the user's query and the retrieved context.
8.  **Display:** The recommendation is displayed to the user in the Streamlit web interface.

## ⚙️ Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/anime-recommender.git
    cd anime-recommender
    ```

2.  **Create a virtual environment and install dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**

    Create a `.env` file in the root directory and add your Groq API key:

    ```
    GROQ_API_KEY="your-groq-api-key"
    ```

4.  **Run the application:**

    ```bash
    streamlit run app/app.py
    ```

## 🐳 Docker

To run the application using Docker:

1.  **Build the Docker image:**

    ```bash
    docker build -t anime-recommender .
    ```

2.  **Run the Docker container:**

    ```bash
    docker run -p 8501:8501 -e GROQ_API_KEY="your-groq-api-key" anime-recommender
    ```

## 📖 Usage

1.  Open your web browser and navigate to `http://localhost:8501`.
2.  In the text box, describe the kind of anime you're in the mood for. For example:
    *   "A high-school romance with a bit of comedy."
    *   "A dark fantasy with a complex magic system."
    *   "A sci-fi anime about space exploration and alien encounters."
3.  The application will then provide you with a personalized anime recommendation.

## 📁 Project Structure

```
.
├── app
│   └── app.py              # Main Streamlit application
├── config
│   └── config.py           # Configuration settings
├── data
│   └── anime_with_synopsis.csv # Dataset
├── pipeline
│   ├── build_pipeline.py   # Script to build the recommendation pipeline
│   └── pipeline.py         # Recommendation pipeline logic
├── src
│   ├── data_loader.py      # Data loading and processing
│   ├── prompt_template.py  # Prompt templates for the LLM
│   ├── recommender.py      # Core recommendation logic
│   └── vector_store.py     # Vector store management
├── utils
│   ├── custom_exception.py # Custom exception handling
│   └── logger.py           # Logging configuration
├── Dockerfile              # Docker configuration
├── llmops-k8s.yaml         # Kubernetes deployment configuration
├── requirements.txt        # Project dependencies
└── setup.py                # Setup script
```

## 🔮 Future Improvements

*   **User Authentication:** Implement user accounts to save recommendation history.
*   **Rating and Feedback:** Allow users to rate recommendations to further personalize the results.
*   **Multi-modal Search:** Enable searching by images or genres in addition to text descriptions.
*   **CI/CD Pipeline:** Set up a CI/CD pipeline for automated testing and deployment.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgments

*   The creators of LangChain, Streamlit, and ChromaDB.
*   The providers of the anime dataset.
