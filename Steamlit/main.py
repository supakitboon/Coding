import streamlit as st
import pandas as pd 
import numpy as np
import utils.func
## check this out 
## https://docs.streamlit.io/develop/api-reference
st.write("Hello")
# Input
# x = st.text_input("Fav Movie?")
x = utils.func.test()
st.write(f"Your fav movie is {x}")
model = utils.func.load_embedding_model()

# show data in graph 
chart_data = pd.DataFrame(np.random.randn(20,3),columns = ["a","b","c"])
st.bar_chart(chart_data)
st.line_chart(chart_data)