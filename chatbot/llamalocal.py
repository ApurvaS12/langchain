from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st 
import os 
from dotenv import load_dotenv

load_dotenv()



#langsmith trackingst
langhcain_tracing = os.environ['LANGCHAIN_TRACING_V2']

langchain_api_key = os.environ['LANGCHAIN_API_KEY']


# prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpfyl assistant.\
          Please response to user queries"),
        ("user", "Question:{question}")

    ]
)


#streamlit framework

st.title("Langchain Demo with Llama")
input_text = st.text_input("Search the topic you want")

# ollama LLama 2 llm

llm = Ollama(model="llama2")
output_parser = StrOutputParser() 
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
