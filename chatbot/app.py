from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.environ['OPENAI_API_KEY']

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

st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want")

# openAI llm

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser() 
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

