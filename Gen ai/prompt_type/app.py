
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered"
)

# Application title
st.title("📝 AI Text Summarizer")
st.write("Summarize long text using Generative AI.")

# User input
user_text = st.text_area(
    "Enter your text:",
    height=250,
    placeholder="Paste your paragraph here..."
)

summary_length = st.selectbox(
    "Select summary length:",
    ["Short", "Medium", "Detailed"]
)

# Prompt Template
template = """
You are an expert text summarizer.

Summarize the following text in a {length} format.

Text:
{text}

Provide a clear and easy-to-understand summary.
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["text", "length"]
)

# Generate button
if st.button("Generate Summary"):

    if not user_text.strip():
        st.warning("Please enter some text.")

    elif not os.getenv("openai_api_key"):
        st.error("API key not found in .env file.")

    else:
        try:
            llm = ChatGroq(
                model="openai/gpt-oss-120b",
                api_key=os.getenv("openai_api_key"),
                temperature=0
            )

            chain = prompt | llm

            with st.spinner("Generating summary..."):

                result = chain.invoke({
                    "text": user_text,
                    "length": summary_length
                })

            st.subheader("Generated Summary")

            st.success(result.content)

        except Exception as e:
            st.error(f"Error: {e}")
