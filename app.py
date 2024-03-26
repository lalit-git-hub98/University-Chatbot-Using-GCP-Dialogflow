import streamlit as st

st.set_page_config(page_title = 'UC Chatbot')

#st.title('Simple ChatBot using LangChain')
st.markdown("<h1 style='text-align:center; color:black;'>University of Cincinnati</h1>", unsafe_allow_html = True)

src = "https://console.dialogflow.com/api-client/demo/embedded/eedef587-810b-4833-a965-02dafd030f2c"

st.components.v1.iframe(src, width=350, height=430)