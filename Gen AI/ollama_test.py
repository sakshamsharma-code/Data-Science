import streamlit as st
import requests
import json

# Streamlit page config
st.set_page_config(page_title="Ollama Chat", page_icon="🤖", layout="centered")

st.title("💬 Ollama Chat with Streamlit")
st.write("Ask anything from the local Ollama model")

# Text input
user_input = st.text_area("✍️ Enter your prompt:", "")

# Button to send
if st.button("🚀 Generate Response"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        url = "http://localhost:11434/api/generate"
        data = {
            "model": "gemma3",
            "prompt": user_input
        }

        # Container to display streaming response
        response_container = st.empty()
        generated_text = ""

        try:
            with requests.post(url, json=data, stream=True) as response:
                for line in response.iter_lines():
                    if line:
                        body = json.loads(line)
                        if "response" in body:
                            generated_text += body["response"]
                            response_container.markdown(generated_text)
        except Exception as e:
            st.error(f"❌ Error: {e}")
