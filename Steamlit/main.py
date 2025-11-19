import streamlit as st
import pandas as pd 
import numpy as np
import utils.func
## check this out 
## https://docs.streamlit.io/develop/api-reference
st.write("Hello")
# Input
# x = st.text_input("Fav Movie?")
x = st.text_input("Your story")
st.write(f"Your fav movie is {x}")
model = utils.func.load_embedding_model()
y = utils.func.get_highlights_with_embeddings(x,1,model,0.47)
st.write(f"Here is your result {y}")


# show data in graph 
chart_data = pd.DataFrame(np.random.randn(20,3),columns = ["a","b","c"])
st.bar_chart(chart_data)
st.line_chart(chart_data)