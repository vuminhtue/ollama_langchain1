from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import streamlit as st

st.sidebar.title("Settings")
llm_name = st.sidebar.selectbox("Model", ["deepseek-r1:1.5b", "llama3.2"])
temperature = st.sidebar.slider("Temperature",0.0,1.0,0.5,0.01)
st.write(llm_name)
st.image("./pony.jpeg")
st.title("AskPeruna")
llm = ChatOllama(base_url="http://localhost:11434", model=llm_name, temperature=temperature)

def my_chatbot(freeform_text):
    prompt = PromptTemplate(
        input_variables="freeform_text",
        template="You are a chatbot. Answer the question carefully. If you dont know say I dont know.\n\n{freeform_text}"
    )

    response=llm.invoke(freeform_text)
    return response.content


freeform_text = st.sidebar.text_area(label="Ask Peruna?",max_chars=100)

if freeform_text:
    response = my_chatbot(freeform_text)
    st.write(response)
