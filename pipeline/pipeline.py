from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    '''Pipeline for building and using the Anime Recommendation System.
    This class initializes the vector store and recommender system, and provides a method to get recommendations based on a user query.
    '''
    def __init__(self, persist_directory: str = "chroma_db"):
        try:
            logger.info("Initializing Anime Recommendation Pipeline...")
            vector_builder = VectorStoreBuilder(csv_path="", persist_directory=persist_directory) # empty csv_path for initialization
            retriever = vector_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)
            logger.info("Anime Recommendation Pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing Anime Recommendation Pipeline: {e}")
            raise CustomException("Error initializing Anime Recommendation Pipeline", e)
        
    def recommend(self, query: str) -> str:
        try:
            logger.info(f"Getting recommendations for query: {query}")
            recommendations = self.recommender.get_recommendations(query)
            logger.info("Recommendations retrieved successfully.")
            return recommendations
        except Exception as e:
            logger.error(f"Error getting recommendations: {e}")
            raise CustomException("Error getting recommendations", e)