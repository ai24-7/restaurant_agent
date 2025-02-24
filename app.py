import streamlit as st
import requests

st.title("Food & Restaurant Assistant")
st.markdown("""
    Ask me about restaurants, menus, pricing, ingredients, or food trends! I'm here to help.
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation turns.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Your Query:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Processing your query..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat/",
                    json={"prompt": prompt},
                    timeout=200
                )
                response.raise_for_status()
                answer = response.json().get("response", "No response received.")
            except requests.RequestException as e:
                answer = f"Error: {e}"
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
