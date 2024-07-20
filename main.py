import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

load_dotenv()
llm = Ollama(model=os.getenv('MODEL_NAME'), base_url=os.getenv('BASE_URL'), verbose=True)

def sendPrompt(prompt):
    global llm
    response = llm.invoke(prompt)
    return response

st.title("Chat with Ollama")
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role":"assistant", "content":"Ask me a question !"}
    ]

if prompt := st.chat_input("Your Question"):
    st.session_state.message.append({"role": "user", "content": prompt})

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = sendPrompt(prompt)
            print(response)
            st.write(response)
            message = {"role":"assistant", "content": response}
            st.session_state.messages.append(message)