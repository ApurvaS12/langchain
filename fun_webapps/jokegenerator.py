from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st 

load_dotenv()

st.title("Jokes Generator")
st.subheader("This Web-app generate funny jokes")

topic = st.text_input(label="enter a topic")

prompt = ChatPromptTemplate.from_template("tell me a dark humoured and funny joke about {topic}")
model = ChatOpenAI()
output_parser =  StrOutputParser()

chain = prompt | model | output_parser

if topic:
    st.info(chain.invoke({'topic': topic}))


