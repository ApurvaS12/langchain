import streamlit as st
import requests

## getting openai response
def get_essay(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
        json = {'input':{'topic': input_text}})
    
    return response.json()['output']['content']

## getting ollama-llama 2 response 
def get_poem(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
        json = {'input': {'topic' : input_text}} )
    
    return response.json()['output']

st.title("Get a essay and a poem on any topic")
st.info("Essay by powered by  openai and Poem by powered by LLama2")

input_text= st.text_input("Write an essay on: ")
if input_text:
    st.write(get_essay(input_text))


input_text1 = st.text_input("Write a poem on: ")
if input_text1:
    st.write(get_poem(input_text1))

