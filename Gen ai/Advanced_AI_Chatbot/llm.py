from langchain_ollama import ChatOllama

def get_model(model_name, temperature):
    llm = ChatOllama(
        model="tinyllama:latest",
        temperature=temperature
    )
    return llm