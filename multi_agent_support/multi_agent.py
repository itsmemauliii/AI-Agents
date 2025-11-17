# deploy_multi_agent.py
import streamlit as st
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from langchain_ollama import ChatOllama

# --- LLM Setup ---
llm = ChatOllama(model="llama3")

# --- Shared State ---
class State(dict):
    pass

# --- Agents ---
def classify_node(state: State):
    text = state.get("input", "")
    prompt = f"Classify this user message into: billing, tech, general. Message: {text}. Return only the category."
    cat = llm.invoke(prompt).content.strip().lower()
    state["category"] = cat
    return state

def billing_agent(state: State):
    msg = state.get("input", "")
    prompt = (
        f"You are a billing-support agent. "
        f"Reply in 1-2 short lines. "
        f"Be clear, concise, and strictly professional. "
        f"Do NOT ask more than one question. "
        f"User message: {msg}"
    )
    state["reply"] = llm.invoke(prompt).content
    return state

def tech_agent(state: State):
    msg = state.get("input", "")
    prompt = f"User issue (technical): {msg}. Give a helpful fix."
    state["reply"] = llm.invoke(prompt).content
    return state

def general_agent(state: State):
    msg = state.get("input", "")
    prompt = f"General question: {msg}. Reply friendly."
    state["reply"] = llm.invoke(prompt).content
    return state

# --- Graph Setup ---
graph = StateGraph(State)
graph.add_node("classifier", classify_node)
graph.add_node("billing", billing_agent)
graph.add_node("tech", tech_agent)
graph.add_node("general", general_agent)
graph.set_entry_point("classifier")

def router(state: State):
    cat = state.get("category")
    if cat == "billing": return "billing"
    if cat == "tech": return "tech"
    return "general"

graph.add_conditional_edges("classifier", router)
memory = MemorySaver()
app_graph = graph.compile(checkpointer=memory)

# --- Streamlit UI ---
st.set_page_config(page_title="Multi-Agent Support", page_icon="💬")
st.title("💬 Multi-Agent Customer Support System")
st.write("Type a message and let our AI handle it!")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    result = app_graph.invoke({"input": user_input})
    reply = result.get("reply", "Sorry, I couldn't process that.")
    
    # Save in history
    st.session_state.history.append({"user": user_input, "bot": reply})
    
    # Clear input
    st.experimental_rerun()

# Display chat
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")
