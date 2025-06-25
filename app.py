import streamlit as st
from chatbot import load_chatbot

st.title("Startup Chatbot 🤖")
query = st.text_input("Ask a question about startups")

if query:
    chatbot = load_chatbot()
    response = chatbot.run(query)
    st.write(response)