import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

# ----------------- Page Config -----------------
st.set_page_config(
    page_title="Anime Recommendation System 🎌",
    page_icon="🎨",
    layout="wide"
)

# ----------------- Load Environment -----------------
load_dotenv()

# ----------------- Init Pipeline -----------------
@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

# ----------------- Custom CSS -----------------
st.markdown("""
    <style>
        .main-title {
            font-size: 2.2rem;
            font-weight: 800;
            text-align: center;
            color: #ff4b4b;
        }
        .sub-text {
            text-align: center;
            font-size: 1rem;
            color: #666;
            margin-bottom: 2rem;
        }
        .recommend-card {
            background-color: #fafafa;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 0.8rem;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# ----------------- Header -----------------
st.markdown('<p class="main-title">🎌 Anime Recommender System 🎨</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Powered by LangChain + RAG | Find your next binge-worthy anime!</p>', unsafe_allow_html=True)

# ----------------- Input -----------------
query = st.text_input(
    "✨ Describe what kind of anime you’re in the mood for:",
    placeholder="Example: Action-packed, time travel, with a strong female lead..."
)

# ----------------- Recommendation Logic -----------------
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)

# ----------------- Sidebar -----------------
with st.sidebar:
    st.header("📖 About This App")
    st.write("""
        This Anime Recommender System uses **LangChain + RAG**  
        to search a knowledge base of anime and give you  
        the most relevant suggestions based on your preferences.  
        
        **Features:**
        - Smart, context-aware recommendations  
        - Built with Python & Streamlit  
        - Powered by LangChain's Retrieval-Augmented Generation
    """)
    st.markdown("---")
    st.caption("💡 Tip: The more detailed your description, the better the results!")
