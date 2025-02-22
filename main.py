import streamlit as st
from agents.agent import MultiToolAgent

def main():
    st.title("Food & Restaurant Assistant")
    st.markdown("""
        Ask me about restaurants, menus, pricing, ingredients, or food trends! I'm here to help.
    """)

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "agent" not in st.session_state:
        st.session_state.agent = MultiToolAgent()

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
                answer = st.session_state.agent.run(prompt)
            st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    main()
