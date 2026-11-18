
import streamlit as st
from llm import get_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Chatbot")
st.caption("Powered by LangChain and Groq")

# Sidebar
with st.sidebar:

    st.header("Settings")

    model_name = st.selectbox(
    "Select Ollama Model",
    [
        "tinyllama"
    ]
)

    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.3
    )

    if st.button("New Chat"):
        st.session_state.messages = []

# Initialize chat history
if "messages" not in st.session_state:

    st.session_state.messages = []

# System instruction
system_message = SystemMessage(
    content="You are a helpful AI assistant. "
            "Give clear and simple answers."
)

# Display previous messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        role = "user"
    else:
        role = "assistant"

    with st.chat_message(role):
        st.markdown(message.content)

# User input
user_input = st.chat_input("Ask anything...")

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Save user message
    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )

    # Create model
    llm = get_model(model_name, temperature)

    # Prepare conversation
    messages = [
        system_message
    ] + st.session_state.messages

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = llm.invoke(messages)

                answer = response.content

                st.markdown(answer)

                st.session_state.messages.append(
                    AIMessage(content=answer)
                )

            except Exception as e:
                st.error(f"Error: {e}")
