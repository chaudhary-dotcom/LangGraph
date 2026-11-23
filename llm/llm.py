from langchain_ollama import ChatOllama

def llm_model():

    model = ChatOllama(
        model='qwen2.5:1.5b',
        temperature=0.3
    )

    return model