import streamlit as st
import sys
sys.path.append('C:/Users/kingm/OneDrive/Desktop/major_project/lib')
from homepage import generate_response
st.page_link("homepage.py", label="Home", icon="🏠")
st.title("Chatbot")
if prompt:= st.chat_input("enter your question"):
    response = generate_response(prompt,2)     
    messages = st.container(height=300)
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(response)
