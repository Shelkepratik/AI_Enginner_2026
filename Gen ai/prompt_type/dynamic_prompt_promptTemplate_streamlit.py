
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="AI Poem Generator")

st.title("AI Poem Generator")
st.write("Generate poems using LangChain and Groq.")

# Prompt Template
prompt = PromptTemplate(
    template="Write a poem about {subject} in a {tone} tone with {lines} lines.",
    input_variables=["subject", "tone", "lines"]
)

# User Input
subject = st.text_input("Enter subject:")

tone = st.selectbox(
    "Select tone:",
    ["Simple", "Medium", "Funny", "Professional"]
)

lines = st.number_input(
    "Enter number of lines:",
    min_value=1,
    max_value=50,
    value=5
)

# Generate
if st.button("Generate Poem"):

    if not subject.strip():
        st.warning("Please enter a subject.")

    elif not os.getenv("GROQ_API_KEY"):
        st.error("GROQ_API_KEY is missing from your .env file.")

    else:
        try:
            llm = ChatGroq(
                model="openai/gpt-oss-120b",
                api_key=os.getenv("openai/gpt-oss-20b"),
                temperature=0.7
            )

            chain = prompt | llm

            with st.spinner("Generating poem..."):
                result = chain.invoke({
                    "subject": subject,
                    "tone": tone,
                    "lines": int(lines)
                })

            st.subheader("Generated Poem")
            st.write(result.content)

        except Exception as e:
            st.error(f"Error: {e}")
