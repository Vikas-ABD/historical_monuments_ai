import streamlit as st
from langchain_core.messages import HumanMessage
from main import get_agent  # Assuming you did step 1!
import uuid

# Initialize agent once
if "orders_agent" not in st.session_state:
    st.session_state.orders_agent = get_agent()

# Create a new thread/session config
if "config" not in st.session_state:
    st.session_state.config = {
        "configurable": {
            "thread_id": str(uuid.uuid4()) 
        }
    }

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "🚛 Welcome to the conversational AI assistant! How can I help you today?"}
    ]

# Streamlit App Layout
st.set_page_config(
    page_title="Historical Monuments Assistant",
    page_icon=None  # No emoji as requested
)

# Page Title and Description
st.title("Historical Monuments Assistant")
st.write("Your friendly AI guide for exploring and learning about famous historical monuments around the world.")

# Optional Welcome Message or Instruction
st.info("Ask me about any historical monument, and I'll share fascinating facts, travel tips, and guides to help you plan your visit!")

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(chat["content"])
    else:
        with st.chat_message("user"):
            st.markdown(chat["content"])

# User input box
if user_input := st.chat_input("Type your message..."):
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Display user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # Format message for agent
    user_message = {"messages": [HumanMessage(user_input)]}

    # Get AI response
    try:
        ai_response = st.session_state.orders_agent.agent_graph.invoke(
            user_message,
            config=st.session_state.config
        )

        # Extract assistant reply
        ai_content = ai_response['messages'][-1].content

        # Add assistant reply to history
        st.session_state.chat_history.append({"role": "assistant", "content": ai_content})

        # Display assistant message
        with st.chat_message("assistant"):
            st.markdown(ai_content)

    except Exception as e:
        error_msg = f"❗️An error occurred: {str(e)}"
        st.session_state.chat_history.append({"role": "assistant", "content": error_msg})
        with st.chat_message("assistant"):
            st.markdown(error_msg)