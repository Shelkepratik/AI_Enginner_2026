from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import load_prompt
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

prompt = load_prompt("notes_template.json")

st.title("📚 Study Notes Generator")

user_topic = st.text_input("Enter the topic:")

user_level = st.selectbox(
    "Choose the level",
    ("Beginner", "Intermediate", "Advanced")
)

user_point = st.number_input(
    "Enter the user point",
    min_value=3,
    max_value=10,
    value=5
)

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("openai_api_key"),
    temperature=0.3
)

if st.button("Generate Notes"):

    if user_topic.strip():

        formatted_prompt = prompt.format(
            topic=user_topic,
            level=user_level,
            points=user_point
        )

        result = llm.invoke(formatted_prompt)

        st.session_state["notes"] = result.content

    else:
        st.warning("Please enter the topic")

# Display notes and feedback
if "notes" in st.session_state:

    st.subheader("Your Notes")
    st.write(st.session_state["notes"])

    st.subheader("Was this answer helpful?")

    feedback = st.feedback("thumbs", key="notes_feedback")

    if feedback == 1:
        st.success("Thank you for your feedback! 👍")

    elif feedback == 0:
        st.info("Thanks for your feedback! 👎")
