import streamlit as st

st.write("Testing model loading...")

try:
    import utils.func
    st.write("Import successful")
    
    st.write("Loading model... (this may take 30-60 seconds)")
    model = utils.func.load_embedding_model()
    st.write("✅ Model loaded successfully!")
    st.write(f"Model type: {type(model)}")
    
except Exception as e:
    st.error(f"Error: {e}")
    import traceback
    st.code(traceback.format_exc())