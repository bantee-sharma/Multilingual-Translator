from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash"
)
st.header("🌍 Multilingual Translator")

# Language slider
languages = ["English", "Hindi", "Japanese", "French", "Spanish", "German", "Chinese"]

col1,col2 = st.columns(2)

with col1:
    source_language = st.selectbox("Select source language:", options=languages, index=0) 

with col2:
    target_language = st.selectbox("Select target language:", options=languages, index=1)

user_input = st.text_area("Enter your text here:")



temp = PromptTemplate(
    template="translate following text to from {source_language} to  {target_language} and return only the translated text:{text}",
    input_variables=["source","language","text"]
)

if st.button("Translate"):
    if user_input.strip():
        chain = temp | model
        res = chain.invoke({"source_language": source_language,"target_language": target_language, "text": user_input})

        if res:
            st.subheader("Translation Result:")
            st.write(res.content)
        else:
            st.error("Error: No response from the model.")
    else:
        st.warning("Please enter some text to translate.")    






