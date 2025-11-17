import streamlit as st
from langchain_ollama import ChatOllama

# --- LLM Setup ---
llm = ChatOllama(model="llama3")

# --- Streamlit UI ---
st.set_page_config(page_title="💬 Multi-Agent Support", page_icon="💬")
st.title("💬 Multi-Agent Customer Support System")
st.write("Type a message and let our AI handle it!")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Get user input
user_input = st.text_input("You:", "")

# Helper functions: classifier + agents
def classify_message(text):
    prompt = f"Classify this user message into: billing, tech, general. Message: {text}. Return only the category."
    category = llm.invoke(prompt).content.strip().lower()
    return category

def billing_agent(text):
    prompt = (
        f"You are a billing-support agent. "
        f"Reply in 1-2 short lines. "
        f"Be clear, concise, and strictly professional. "
        f"Do NOT ask more than one question. "
        f"User message: {text}"
    )
    return llm.invoke(prompt).content

def tech_agent(text):
    prompt = f"User issue (technical): {text}. Give a helpful fix."
    return llm.invoke(prompt).content

def general_agent(text):
    prompt = f"General question: {text}. Reply friendly."
    return llm.invoke(prompt).content

# Send button
if st.button("Send") and user_input:
    # Step 1: Classify
    category = classify_message(user_input)

    # Step 2: Route to appropriate agent
    if category == "billing":
        reply = billing_agent(user_input)
    elif category == "tech":
        reply = tech_agent(user_input)
    else:
        reply = general_agent(user_input)

    # Step 3: Save in chat history
    st.session_state.history.append({"user": user_input, "bot": reply})
    st.experimental_rerun()

# Display chat history with colors & emojis
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    if "billing" in chat['bot'].lower():
        st.markdown(f"💳 **Bot:** {chat['bot']}")
    elif "fix" in chat['bot'].lower() or "technical" in chat['bot'].lower():
        st.markdown(f"🛠️ **Bot:** {chat['bot']}")
    else:
        st.markdown(f"☀️ **Bot:** {chat['bot']}")
    st.markdown("---")
