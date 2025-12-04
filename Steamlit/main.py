import streamlit as st
import pandas as pd 
import numpy as np
import utils.func
## check this out 
## https://docs.streamlit.io/develop/api-reference
st.write("Hello")
# Input
# x = st.text_input("Fav Movie?")
# x = st.text_input("Your story")
# st.write(f"Your fav movie is {x}")
# model = utils.func.load_embedding_model()
# y = utils.func.get_highlights_with_embeddings(x,1,model,0.47)


# Create analysis results
sentences = ["White people take up the majority of all jobs, showing discrimination in the workplace, and a lack of opportunities for people of color.",
"Whites in every category make up the majority of the workforce in STEM occupations.",
"Although Hispanics make up the second-most majority of the workforce overall, they have very little representation in the STEM field."
]
predictions = [1,0,1]
analysis_results = []
model= utils.func.load_embedding_model()
    
for sentence, pred in zip(sentences, predictions):
    result = utils.func.get_highlights_with_embeddings(
        sentence, 
        pred,  # 1 for Show, 2 for Tell
        model, 
        threshold=0.47
    )
    analysis_results.append({
        'sentence': sentence,
        'type': result['stage'],
        'highlights': result['highlights']
    })

st.write(analysis_results)

TYPE_MAP = {0: "Show", 1: "Tell"}
if st.button("Get AI Explanations"):
    with st.spinner("Getting explanations..."):
        for i, result in enumerate(analysis_results):
            sentence = result['sentence']
            type_name = result['type']
            highlights = result['highlights']
            # Create prompt for this sentence
            prompt = f"""
            
            You are an expert in data/story telling.
            Definitions:
            - "Show" statements are DESCRIPTIVE - they describe what is visible in the data/chart
            - "Tell" statements are INTERPRETIVE - they make claims, interpretations, or conclusions beyond what's directly visible
            Explain in 2-3 sentences why this sentence is classified as "{type_name}":      
            Sentence: "{sentence}". 
            """
            
            # Call OpenRouter API
            response = utils.func.call_openrouter_llm(prompt, api_key)
            # Display results
            st.write(f"**Sentence {i+1}:** {sentence}")
            st.info(f"**Classification:** {type_name}")
            st.info(f"**Highlight words:** {highlights}")
            st.success(f"**Explanation:** {response}")
            st.write("---")