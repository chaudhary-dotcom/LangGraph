from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from llm.model import llm_model
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages


llm = llm_model()

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# tools
def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {'messages': [response]}

# Checkpointer
checkpointer = InMemorySaver()

# workflow 
graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)

