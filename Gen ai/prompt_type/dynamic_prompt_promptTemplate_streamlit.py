
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

tmpl = "write a poem about {subject} in a {tone} tone with {lines} lines"

prompt_obj = PromptTemplate(
    template=tmpl,
    input_variables=["subject", "tone", "lines"]
)

st.title("poem Genratore")

user_subject = st.text_input("provide a subject")
user_tone = st.text_input("provide the tone:")
user_lines = st.text_input("Enter the lines of poem to create:",min_value=1,max_value=50)

complete_prompt = prompt_obj.invoke(
    {
        "subject": user_subject,
        "tone": user_tone,
        "lines": user_lines
    }
)

final_prompt = complete_prompt.text

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("openai_api_key"),
    temperature=0
)

if st.button("Generate"):
    if final_prompt:
        result = llm.invoke(final_prompt)
        st.write(result.content)
    else:
        st.warning("please submit your question")
