from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)
'''Pipeline for building and using the Anime Recommendation System. It creates a vector store from a CSV file and initializes the recommender system.'''
def main():
    try:
        logger.info("Starting Anime Recommendation Pipeline...")
        # Load and process the anime data
        data_loader = AnimeDataLoader(original_csv="data/anime_with_synopsis.csv", processed_csv="data/processed_anime.csv")
        processed_csv = data_loader.load_and_process() 
        logger.info(f"Data loaded and processed successfully. Processed file: {processed_csv}")
        vector_builder = VectorStoreBuilder(csv_path=processed_csv)
        vector_builder.build_and_save_vector_store()
        logger.info("Vector store built and saved successfully.")
        logger.info("Anime Recommendation Pipeline completed successfully.")
    except Exception as e:
        logger.error(f"Error in Anime Recommendation Pipeline: {e}")
        raise CustomException("Error in Anime Recommendation Pipeline", e)
    
if __name__ == "__main__":
    main()