import openai 
import streamlit as st

# pip install streamlit-chat  
from streamlit_chat import message
openai.api_key = st.secrets["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"]
def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message 
  #Creating the chatbot interface
st.title("Musebot")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


