from sentence_transformers import SentenceTransformer

def test ():
    return 2

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

